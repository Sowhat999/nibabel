#!/usr/bin/env python3
import sys
import tomli
from pathlib import Path

if sys.version_info < (3, 6):
    print("This script requires Python 3.6 to work correctly")
    sys.exit(1)

repo_root = Path(__file__).parent.parent
pyproject_toml = repo_root / "pyproject.toml"
reqs = repo_root / "requirements.txt"
min_reqs = repo_root / "min-requirements.txt"

with open(pyproject_toml, 'rb') as fobj:
    config = tomli.load(fobj)
requirements = config["project"]["dependencies"]

script_name = Path(__file__).relative_to(repo_root)

lines = [f"# Auto-generated by {script_name}", ""]

# Write requirements
lines[1:-1] = requirements
reqs.write_text("\n".join(lines))

# Write minimum requirements
lines[1:-1] = [req.replace(">=", "==").replace("~=", "==") for req in requirements]
min_reqs.write_text("\n".join(lines))
