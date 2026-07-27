#!/bin/bash

# 1. cd into project folder
cd ~/portfolio-project || exit 1

# 2. Pull the latest changes from GitHub main
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yaml down

docker compose -f docker-compose.prod.yaml up -d --build
