## Configuration

- Before `pyproject.toml`:

```
setup.py          # Build configuration
setup.cfg         # Metadata (sometimes)
requirements.txt  # Dependencies
MANIFEST.in       # File inclusion
tox.ini          # Testing config
```

- After `pyproject.toml`:

```
[build-system]           # PEP 518
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]                # PEP 621
name = "my-package"
version = "1.0.0"
dependencies = ["requests"]

[tool.setuptools]        # Tool-specific sections
packages = ["src"]

[tool.black]             # Other tools use [tool.*]
line-length = 88
```

- Or with mixed project configuration:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-fullstack-app"
version = "1.0.0"
description = "FastAPI + Node.js application"

[tool.hatch.envs.backend]
dependencies = [
    "fastapi",
    "uvicorn",
    "pytest"
]

[tool.hatch.envs.frontend]
dependencies = []  # Node deps managed by package.json

[tool.hatch.scripts]
start-backend = "uvicorn backend.main:app --reload"
start-frontend = "cd frontend && npm start"
start = ["start-backend", "start-frontend"]
```

To define dependency groups that can be installed, use `[project.optional-dependencies]`. Example:  `pip install -e .[dev]` or `pip install -e .[dev,docs]`

**Note**: If you don't build a Python package, but a mixed project between backend and frontend, you likely don't need `[tool.hatch.build.targets.*]` at all — those are for publishing to PyPI.
