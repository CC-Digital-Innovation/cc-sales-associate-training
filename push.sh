#!/bin/bash -e
git stash
git pull
git stash apply
commit_message="$1"
git add . -A
git commit -m "$commit_message"
git push
