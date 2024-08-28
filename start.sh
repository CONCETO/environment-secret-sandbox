#!/bin/bash

# Load environment variables from .env file
source .env

# Build the Docker image
docker build -t env-secret-creator -f Dockerfile .

# Run the Docker container
docker run --rm \
  -v $(pwd)/create_envs_and_secrets.py:/app/create_envs_and_secrets.py \
  -e GITHUB_TOKEN=$GITHUB_TOKEN \
  env-secret-creator
