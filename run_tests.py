#!/usr/bin/env python3
"""
Simple test runner script for the project.
"""
import subprocess
import sys
from pathlib import Path

def run_tests():
    """Run pytest with appropriate configuration."""
    project_root = Path(__file__).parent
    
    # Change to project root directory
    import os
    os.chdir(project_root)
    
    # Run pytest
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "--tb=short",
        "--strict-markers"
    ]
    
    print(f"Running tests from: {project_root}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 50)
    
    result = subprocess.run(cmd)
    return result.returncode

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)

