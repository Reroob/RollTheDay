"""
Pytest configuration and shared fixtures for the test suite.
"""
import pytest
import sys
from pathlib import Path

# Add the project root to Python path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

@pytest.fixture(scope="session")
def project_root_path():
    """Provide the project root path for tests."""
    return Path(__file__).parent.parent

