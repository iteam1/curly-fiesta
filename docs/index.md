# Curly Fiesta

Exploring modern Python packaging with `pyproject.toml`.

## Quick Start

```bash
# Install all dependencies
uv sync --extra dev --extra docs

# Run the CLI
curly-fiesta

# Run tests
uv run pytest

# Serve docs
uv run mkdocs serve
```

## Diagrams

```kroki-mermaid
graph TD
    A[pyproject.toml] --> B[hatchling]
    B --> C[curly_fiesta package]
    A --> D[uv sync]
    D --> E[.venv]
```
