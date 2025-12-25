# Copilot / AI Agent Instructions — 30DaysOfPython

Short, actionable guidance to help an AI agent contribute safely and productively to this repository.

## Project overview
- This is a small, educational repository of Python exercises organized by day in top-level folders (`day_1/`, `day_2/`, `day_3/`). Files are primarily short scripts and simple functions meant for demonstration and practice (e.g., `day_1/euclidean.py`, `day_2/variables.py`, `day_3/main.py`).
- Code style is script-first (interactive `input()` + `print()`), with occasional small helper functions (e.g., `calculate_intercepts` in `day_3/main.py`). Expect minimal external tooling or dependencies.

## What to expect when making changes
- Keep changes small, focused, and easily reviewable (single concept per PR). These files are learning exercises — prefer clarity and didactic examples over heavy refactors.
- Preserve interactive behavior when the intent is to demonstrate console input/output; when adding tests, prefer extracting pure functions and parameterizing logic instead of keeping `input()` inside testable code.
- Follow existing naming and formatting patterns: snake_case variables and readable, explicit code (e.g., `radius_circle`, `area_rect`, `calculate_intercepts`). Use f-strings for formatted output.

## Running and debugging
- Scripts run with the system Python: `python day_3/main.py` (Windows PowerShell or cmd). There is no project-level entrypoint or packaging.
- When debugging, run the specific day script or use a small wrapper that calls functions with deterministic inputs instead of using blocking `input()` calls.

## Project-specific guidance and examples
- Replace interactive I/O with parameterized functions for unit testing. Example conversion hint (do not apply automatically):
  - Current pattern (in `day_2/variables.py`):
    - `user_radius = float(input("Enter the radius of the circle: "))`
    - `user_area = math.pi * user_radius ** 2`
  - Recommended testable pattern:
    - ``def area_of_circle(radius: float) -> float: return math.pi * radius ** 2``
    - Then tests can call `area_of_circle(2.0)` and assert expected output.

- Watch for small bugs and typos found in code; call them out explicitly in PRs rather than silently fixing multiple files.
  - Example discovered issue in `day_3/main.py`: `area_circ = math.pi ** 2` is incorrect — it should be `math.pi * radius_circle ** 2`.
  - Example comment typo: `# 11 alculate the value of y` (missing "C").

- Favor pure-Python, no-dependency solutions unless a clear educational purpose needs a dependency (in that case, add instructions to `README.md` and a requirements file).

## Tests and CI (current state)
- There are no tests or CI configuration in the repository. If adding tests, use `pytest` and create a top-level `tests/` directory that mirrors the `day_*` layout (e.g., `tests/test_main.py`).
- When adding CI, keep configs minimal (GitHub Actions with a single job that installs Python, runs `pytest`). Include a `requirements-dev.txt` only if you add non-standard test tools.

## PR & commit etiquette for an agent
- Make focused commits with short messages like `fix(day_3): correct circle area calculation` or `feat(test): add unit tests for area_of_circle`.
- In PR description, explain intent and list the files changed, the reason for the change, and any manual testing steps (e.g., `Run: python day_3/main.py and enter 3 for radius`).

## What *not* to do automatically
- Do not convert all interactive scripts to functions in a single sweep — prefer incremental, well-tested refactors.
- Avoid introducing third-party packages without a clear reason and explicit documentation.

## Useful files & locations (examples)
- `day_1/euclidean.py` — simple math example computing Euclidean distance.
- `day_2/variables.py` — examples of types, arithmetic, and console input for circle calculations.
- `day_3/main.py` — mixed content: functions, interactive prompts, and small bugs (see note above).

---
If any part of this is unclear or you'd like more detail (for example, a suggested test scaffold or a sample GitHub Actions workflow), tell me which section to expand and I'll iterate. Please confirm whether you want me to open a PR with these changes. 
