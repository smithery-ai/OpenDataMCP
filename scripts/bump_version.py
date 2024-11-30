#!/usr/bin/env python
import re
import sys
from pathlib import Path

def bump_version(version_type):
    init_file = Path("src/osmcp/__init__.py")
    
    # Read current version
    content = init_file.read_text()
    current_version = re.search(r'__version__ = ["\']([^"\']+)["\']', content).group(1)
    major, minor, patch = map(int, current_version.split('.'))
    
    # Update version based on argument
    if version_type == "major":
        new_version = f"{major + 1}.0.0"
    elif version_type == "minor":
        new_version = f"{major}.{minor + 1}.0"
    elif version_type == "patch":
        new_version = f"{major}.{minor}.{patch + 1}"
    else:
        print("Invalid version type. Use 'major', 'minor', or 'patch'")
        sys.exit(1)
    
    # Update __init__.py
    new_content = re.sub(
        r'__version__ = ["\']([^"\']+)["\']',
        f'__version__ = "{new_version}"',
        content
    )
    init_file.write_text(new_content)
    
    print(f"Version bumped from {current_version} to {new_version}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bump_version.py <major|minor|patch>")
        sys.exit(1)
    
    bump_version(sys.argv[1])
