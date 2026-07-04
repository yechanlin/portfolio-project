#!/bin/bash

# 1. Kill all existing tmux sessions
tmux kill-server 2>/dev/null

# 2. cd into project folder
cd ~/portfolio-project || exit 1

# 3. Pull latest changes from GitHub
git fetch && git reset origin/main --hard

# 4. Enter venv and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 5. Start a new detached tmux session running the Flask server
tmux new-session -d -s portfolio "cd ~/portfolio-project && source python3-virtualenv/bin/activate && export FLASK_ENV=development && flask run --host=0.0.0.0"
