# 📘 Assignment: Testing Python Programs with pytest

## 🎯 Objective

Practice writing and running automated tests with pytest. You will test a small gradebook module, use edge cases to find bugs, and correct the code while keeping the tests passing.

## 📝 Tasks

### 🛠️ Run the Starter Tests

#### Description
Install pytest, review the documented behavior in `gradebook.py`, and run the starter tests to see how pytest reports results.

#### Requirements
Completed program should:

- Install pytest with `python -m pip install pytest`
- Run the tests from this assignment folder with `python -m pytest -v`
- Confirm that the provided starter tests pass


### 🛠️ Test Normal and Edge Cases

#### Description
Add tests to `test_gradebook.py` for cases not covered by the starter tests. Include average scores that produce a decimal and an empty score list, as well as grade and passing-score boundaries.

#### Requirements
Completed program should:

- Test that an average retains its fractional part and that an empty list returns `0`
- Test that a score of `90` receives an `"A"` and a score of `60` counts as passing
- Use clear test names and run the tests with pytest


### 🛠️ Find and Fix the Bugs

#### Description
Run the expanded tests, use their failure messages to locate the problems in `gradebook.py`, then correct the functions without changing their documented behavior.

#### Requirements
Completed program should:

- Correctly calculate arithmetic averages, including fractional results
- Apply the documented grade and passing-score boundaries
- Pass all tests in `test_gradebook.py`
