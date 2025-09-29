# Tests for RollTheDay

This directory contains unit tests for the RollTheDay application.

## Test Structure

- `test_taskgenerator_utils.py` - Unit tests for the task generator utilities
- `conftest.py` - Pytest configuration and shared fixtures
- `__init__.py` - Package initialization

## Running Tests

### Using pytest directly:
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_taskgenerator_utils.py

# Run with verbose output
uv run pytest -v

# Run specific test class
uv run pytest tests/test_taskgenerator_utils.py::TestCalculateSubtaskWeight

# Run specific test method
uv run pytest tests/test_taskgenerator_utils.py::TestCalculateSubtaskWeight::test_empty_subtasks_returns_category_as_selectable_task
```

### Using the test runner script:
```bash
uv run python run_tests.py
```

## Test Coverage

The tests cover:

### `calculate_subtask_weight` function:
- Empty subtasks list (returns category as SelectableTask)
- Non-empty subtasks list (converts all subtasks to SelectableTasks)
- Proper weight calculations
- Error handling for edge cases

### `convert_category_to_selectabletask` function:
- Correct conversion of TaskCategoryRead to SelectableTask
- Proper attribute mapping (ratioweight, tasktype, prioritypending)
- Modification of original category object

### `convert_subtask_to_selectabletask` function:
- Correct conversion of SubTasksRead to SelectableTask
- Proper weight ratio calculation
- Attribute mapping and modification

### `calculate_subtask_weight` (ratio calculation):
- Correct weight ratio calculations
- Edge cases (zero weights, high weights)
- Mathematical accuracy

## Test Data

Tests use realistic test data with:
- Valid UUIDs for public_id fields
- Appropriate weight values
- Various priority and limit settings
- Different color codes

## Mocking

Tests use `unittest.mock` to:
- Mock external function calls
- Isolate units under test
- Control return values for testing different scenarios

## Fixtures

Common test data is provided through pytest fixtures:
- `sample_category` - Sample TaskCategoryRead object
- `sample_subtask` - Sample SubTasksRead object  
- `sample_category_subtask_list` - Combined category and subtask list

## Notes

- Tests are designed to be independent and can run in any order
- Each test method tests a single behavior or scenario
- Edge cases and error conditions are covered
- Tests verify both return values and side effects (object modifications)

