# Copilot instructions

## Project overview

This is a small Finnish-language shopping-cart domain exercise. The domain is
split into three collaborating classes:

- `Tuote` (`src/tuote.py`) represents a product and owns its name and unit price.
- `Ostos` (`src/ostos.py`) wraps a product in a cart line, tracks quantity, and
  calculates the line total.
- `Ostoskori` (`src/ostoskori.py`) is the cart aggregate and is responsible for
  adding, removing, clearing, listing, and totaling cart contents.

`src/index.py` is currently only a placeholder for possible test code. The
tests live in `src/tests/` and exercise the cart through its public methods.
`Ostoskori` is intentionally incomplete, so changes should preserve the
exercise's test-driven progression rather than adding unrelated application
layers.

## Build, test, and lint

The project targets Python 3.14 (`.python-version`) and declares pytest as a
development dependency in `pyproject.toml`. Use uv so the declared environment
and dependencies are selected:

```powershell
uv run pytest -q
```

Run one test by specifying the module, class, and method:

```powershell
uv run pytest -q src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

No separate build or lint command is configured in this project.

## Change constraints

- Do not change `src/ostos.py` or `src/tuote.py`.
- Do not edit tests unless explicitly asked to do so.
- Always only implement the absolutely minimal code change that makes the tests
  pass. Do not add any code that is not strictly necessary for the tests to pass, even if it seems like a good idea.

## Code conventions

- Keep domain identifiers and test names in Finnish, matching the existing
  public API (`Tuote`, `Ostos`, `Ostoskori`, `lisaa_tuote`, `hinta`, etc.).
- Tests use `unittest.TestCase` and `setUp`, and are executed by pytest.
  Add cart behavior tests under `src/tests/` only when explicitly asked.
- The source modules use flat imports such as `from tuote import Tuote`.
  Preserve this layout and use the project-root pytest commands above rather
  than introducing a package hierarchy without a repository-wide reason.
- `Ostos` starts with quantity 1; quantity changes are integer deltas and are
  clamped at zero. Its price is quantity multiplied by the wrapped product's
  unit price.
- `Tuote` stores integer prices and exposes them through `hinta()`; use the
  existing methods and data model when implementing cart behavior.
