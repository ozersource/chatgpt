#!/bin/sh

echo '清除Push记录，并push到github'
git add -A
git checkout main
git checkout --orphan new_branch
git commit -m $(date +"%Y\%m\%d-%H:%m:%S")
git branch -D main
git branch -m main
git push -f origin main
git push --set-upstream origin main
git reflog expire --expire=now --all
git gc --prune=now
