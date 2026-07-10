#!/bin/bash

# 1. cd into project folder
cd ~/portfolio-project || exit 1

# 2. Pull the latest changes from GitHub main
git fetch && git reset origin/main --hard

# 3. Enter venv and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 4. Restart the systemd service to load the new code
sudo systemctl restart myportfolio
