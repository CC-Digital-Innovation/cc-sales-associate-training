@echo off

echo Push to GitHub/GitLab
echo.

git stash
git pull
git stash apply
set /p comment="Enter comment: "
git.exe add .
git.exe commit -m "%comment%"
git.exe push

echo.
echo All done :)

pause
