#!/bin/bash

# Ignore these files. They are local settings and you don't want to update
# them when you checkout the master branch.
# Only use this command once when you setup your dev env.
git update-index --skip-worktree ./.vscode/settings.json
