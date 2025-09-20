# Copilot Instructions for Algo_practice

## Project Overview
This repository contains Python scripts for practicing algorithm problems, organized by difficulty:
- `Easy_prac.py`: Easy-level problems
- `Med_prac.py`: Medium-level problems
- `Hard_prac.py`: Hard-level problems
- `Test.py`: Used for testing solutions

## Architecture & Patterns
- Each script contains standalone functions for individual problems. There is no shared module structure or class-based architecture.
- Functions are typically named after the problem or its main concept (e.g., `two_sum`, `longest_substring`).
- Solutions are self-contained; cross-file imports are rare or absent.
- The codebase is flat, with all scripts in the root directory.

## Developer Workflows
- **Testing:** Use `Test.py` to manually or programmatically test functions from the other scripts. There is no formal test framework (e.g., pytest) unless added.
- **Debugging:** Add print statements or use Python's built-in debugger (`pdb`) for troubleshooting.
- **Execution:** Run scripts directly using `python <scriptname>.py` from the command line.

## Conventions
- Function signatures should be clear and use standard Python types.
- Avoid global state; prefer passing all required data as function arguments.
- Document each function with a brief comment describing the problem and approach.
- Group related problems together within each file for easier navigation.

## Integration Points
- No external dependencies are present by default. If a package is required, add an import at the top of the relevant script and document its use.
- No API integrations or external services are used.

## Example Patterns
```python
# Example function in Med_prac.py
# Problem: Find the longest substring without repeating characters
# Approach: Sliding window

def longest_substring(s: str) -> int:
    # ...implementation...
    return result
```

## Key Files
- `Easy_prac.py`, `Med_prac.py`, `Hard_prac.py`: Main solution files
- `Test.py`: For testing and validation

## AI Agent Guidance
- When adding new problems, follow the existing function-based pattern and place them in the appropriate file by difficulty.
- When updating solutions, preserve existing function signatures unless a change is required for correctness.
- If introducing new workflows (e.g., automated tests), document them in this file and in `Test.py`.

---
For questions or unclear conventions, ask for clarification or review recent changes for emerging patterns.
