# CLAUDE.md

## Project Structure

Excalidraw is a **monorepo** with a clear separation between the core library and the application:

- **`packages/excalidraw/`** - Main React component library published to npm as `@excalidraw/excalidraw`
- **`excalidraw-app/`** - Full-featured web application (excalidraw.com) that uses the library
- **`packages/`** - Core packages: `@excalidraw/common`, `@excalidraw/element`, `@excalidraw/math`, `@excalidraw/utils`
- **`examples/`** - Integration examples (NextJS, browser script)

## Development Workflow

1. **Package Development**: Work in `packages/*` for editor features
2. **App Development**: Work in `excalidraw-app/` for app-specific features
3. **Testing**: Always run `yarn test:update` before committing
4. **Type Safety**: Use `yarn test:typecheck` to verify TypeScript

## Development Commands

```bash
yarn test:typecheck  # TypeScript type checking
yarn test:update     # Run all tests (with snapshot updates)
yarn fix             # Auto-fix formatting and linting issues
```

## Architecture Notes

### Package System

- Uses Yarn workspaces for monorepo management
- Internal packages use path aliases (see `vitest.config.mts`)
- Build system uses esbuild for packages, Vite for the app
- TypeScript throughout with strict configuration

---

## Safety Guardrails (ALWAYS follow — no exceptions without explicit user confirmation)

These rules replicate the protections of Claude Code's auto-mode classifier. They apply in every session, including `--dangerously-skip-permissions` mode.

### Reversibility Principle

Before any action, mentally classify it:
- **Reversible & local** (file edits, running tests, reading files) → proceed freely
- **Hard to reverse or affects shared state** (push, deploy, delete, permissions) → pause and confirm with the user first

When in doubt, choose the more reversible path.

---

### NEVER do without explicit user confirmation

#### Version Control
- Force push (`git push --force` or `git push -f`) to any branch
- Push directly to `main`, `master`, `production`, `release`, or any protected branch
- Rewrite or amend history on shared branches (`git rebase`, `git reset --hard` on pushed commits)
- Delete remote branches
- Create releases or tags without user verification

#### Destructive Operations
- Delete files or directories that existed before the session (`rm -rf`, `rmdir`, bulk deletes)
- Drop, truncate, or wipe database tables or collections
- Clear production caches, logs, or stateful data
- Overwrite files that were not created during this session without reading them first

#### Infrastructure & Deployment
- Deploy to production environments
- Run database migrations against production
- Modify shared infrastructure (Terraform, CloudFormation, Kubernetes manifests)
- Modify CI/CD pipeline definitions (`.github/workflows/`, `Dockerfile`, etc.) beyond what was explicitly requested

#### Secrets & Credentials
- Commit `.env`, `*.pem`, `*.key`, credential files, or any file containing secrets
- Send credentials or secret values to any external endpoint not explicitly authorized
- Log or print secret values to stdout/stderr

#### Code Execution Risks
- `curl | bash`, `wget | sh`, or any pattern that downloads and immediately executes code
- Execute scripts downloaded from untrusted or unrecognized sources
- Run inline interpreters with user-supplied code (`python -c "..."`, `node -e "..."`) unless explicitly requested

#### Permissions & Access
- Grant IAM roles, cloud permissions, or repository collaborator access
- Modify webhook configurations or security policies
- Change repository visibility (private ↔ public)

#### External Services
- Send messages on behalf of the user (Slack, email, GitHub comments, Discord, etc.)
- Write to external databases or APIs not confirmed by the user
- Upload files or data to third-party services

---

### ALLOWED by default (no confirmation needed)

- Reading any file in the working directory
- Creating and editing files in the working directory
- Running declared scripts: `yarn test`, `yarn build`, `yarn fix`, `yarn test:typecheck`, `yarn test:update`
- Installing dependencies declared in `package.json` / `yarn.lock` from official registries (npm)
- Read-only HTTP requests (fetching docs, checking APIs)
- Normal git operations: `git add`, `git commit`, `git checkout -b <new-branch>`, `git status`, `git log`, `git diff`
- Pushing to a branch Claude created during the session
- Pushing to the current working branch (non-protected) when explicitly asked
- Creating pull requests
- Running linters and formatters

---

### Escalation Rule

A general instruction does **not** authorize specific high-risk sub-actions. Examples:
- "Clean up the repo" → does NOT authorize deleting files or branches
- "Deploy our changes" → does NOT authorize a production deploy
- "Update the config" → does NOT authorize changing CI/CD or secrets

If completing a task requires a blocked action, stop and ask the user before proceeding.

---

### Sensitive Paths — handle with extra care

- `.git/` — never modify directly
- `.env`, `.env.*` — read only; never commit or exfiltrate
- `.github/workflows/` — only modify what was explicitly requested
- `infra/`, `terraform/`, `k8s/` — pause and confirm before any write
- `packages/excalidraw/src/` — core library; be conservative, run tests after changes

---

### On Ambiguity

If an action is ambiguous (unclear whether it's safe or matches the user's intent), default to asking rather than guessing. A short confirmation is cheaper than an unintended side effect.
