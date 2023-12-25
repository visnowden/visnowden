#!/bin/bash

echo "\nls -la"
ls -la
git add snake/
git commit -m "Update snakes's SVG files to output"

# Fetch the latest changes from the remote
git fetch

# Pull the changes from the remote
git pull origin output

# Push da nova branch local para a remota
git push origin HEAD:output
