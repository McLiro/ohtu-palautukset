# Copilot instructions

## Build, test, and lint

- Use Python 3.14 and the checked-in `uv.lock`. From this directory, install the environment with `uv sync`.
- Start the Flask server in one terminal with `uv run python src/index.py`. It listens on `http://localhost:5001`.
- Run the complete browser acceptance suite from a second terminal with `uv run robot src/tests`.
- Run one test case with `uv run robot --test "Login With Correct Credentials" src/tests/login.robot`. Replace the test name and suite path as needed. The server must already be running.
- There is no configured build step or linter in `pyproject.toml`; do not add a lint command unless a linter is introduced.
- Robot runs generate `output.xml`, `log.html`, `report.html`, `browser/`, and `playwright-log.txt`; these are ignored by Git.

## Architecture

- `src/index.py` is the development entry point. It imports the Flask application from `src/app.py` and starts it on port 5001.
- `src/app.py` owns HTTP routes and presentation flow. GET routes render Jinja templates; POST handlers read form fields, call `user_service`, flash exception messages, and redirect to the appropriate page.
- `src/services/user_service.py` contains validation, registration, and credential-checking rules. It receives a repository through its constructor, which keeps the service testable, while the module-level `user_service` uses the default repository.
- `src/repositories/user_repository.py` is an in-memory store. The module-level `user_repository` is shared by the Flask app and is reset through `POST /tests/reset`, which the acceptance tests call before each test.
- `src/entities/user.py` contains the simple `User` entity. Templates under `src/templates` provide the page titles and form field IDs asserted by the browser suites.
- `src/tests` contains Robot Framework suites using Browser/Playwright. `resource.robot` defines shared URLs, browser setup, selectors, and keywords; `AppLibrary.py` provides HTTP helpers for resetting state and creating fixture users.

## Repository-specific conventions

- Keep application imports rooted at `src`: the server is launched as `src/index.py`, and Robot imports `../AppLibrary.py` from `src/tests`.
- Preserve the existing route and form contracts when changing UI or handlers. Browser tests depend on routes such as `/login`, `/register`, `/tests/reset`, element IDs `username`, `password`, and `password_confirmation`, and exact page titles.
- User-facing validation/authentication failures are surfaced through Flask flash messages and a redirect back to the relevant form. Keep the existing message text stable when behavior is unchanged because Robot tests assert those messages.
- Acceptance tests isolate themselves with `POST /tests/reset`; setup keywords then create only the fixture users needed by that suite. Keep reset behavior deterministic when changing persistence.
- Add shared browser actions and selectors to `src/tests/resource.robot`; keep suite-specific setup and assertions in the relevant `home.robot`, `login.robot`, or `register.robot` file.
- The repository is intentionally in-memory for this exercise. Do not assume users persist across server restarts or tests, and do not introduce a database-backed lifecycle without updating the reset/test setup contract.
