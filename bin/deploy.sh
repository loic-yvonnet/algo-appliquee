#!/bin/bash

# Note: This is *not* the preferred way to deploy but rather a reminder of the manual steps
#       in case there is a problem with GitHub Actions workflows in the future.

# Local variables
script_dir="$(dirname "$0")"
root_dir="$(dirname "${script_dir}")"
above_root_dir="$(dirname "${root_dir}")"

# Check existence
if [ ! -d "${root_dir}" ]
then
    echo "Error: ${root_dir} does not exist."
    exit 1
fi
if [ ! -d "${above_root_dir}" ]
then
    echo "Error: ${above_root_dir} does not exist."
    exit 1
fi

# Check if the current user has write permission
if [ ! -w "${above_root_dir}" ]
then
    echo "Error: You do not have write permission for ${above_root_dir}."
    exit 1
fi

# Go to the main branch and build the code
echo "Switching to the main branch..."
git checkout main
if [ $? -ne 0 ]
then
    echo "Error: Failed to switch to the main branch."
    echo "Your working directory should be clean and ready to deploy."
    exit 1
fi

echo "Checking dependencies..."
npm i
if [ $? -ne 0 ]
then
    echo "Error: Failed to install the dependencies."
    exit 1
fi

echo "Recompiling..."
npm run -s build
if [ $? -ne 0 ]
then
    echo "Error: Failed to build the project."
    exit 1
fi

# Move the build output directory above the git-tracked root directory
mv ${root_dir}/dist ${above_root_dir}
if [ $? -ne 0 ]
then
    echo "Error: Failed to move the build output directory."
    exit 1
fi

# Switch to the GitHub Pages branch, which holds the distributed code
# Note: This script is deleted while switching to this branch.
#       Even if this file is deleted, the script will continue to execute
#       because it is running from memory, not directly from the file.
git checkout gh-pages
if [ $? -ne 0 ]
then
    echo "Error: Failed to switch to the GitHub Pages gh-pages branch."
    exit 1
fi

# Clean-up everything
find "${root_dir}" -path "${root_dir}/.git" -prune -o -exec rm -rf {} +
if [ $? -ne 0 ]
then
    echo "Error: Failed to clean the GitHub Pages gh-pages branch."
    exit 1
fi

# Move the result of the last build into the GitHub Pages branch
mv ${above_root_dir}/dist/* "${root_dir}"
if [ $? -ne 0 ]
then
    echo "Error: Failed to move the build outputs to the gh-pages branch."
    exit 1
fi

# Remove the dist directory above root - it is not empty
rm -rf "${above_root_dir}/dist"
if [ $? -ne 0 ]
then
    echo "Error: Failed to remove the dist directory."
    exit 1
fi

# Add changes to the staging area
git add -A
if [ $? -ne 0 ]
then
    echo "Error: Failed to add changes to the staging area."
    exit 1
fi

# Commit changes
git commit -m "Update GitHub Pages"
if [ $? -ne 0 ]
then
    echo "Error: Failed to commit changes."
    exit 1
fi

# Push the changes to the remote origin
git push
if [ $? -ne 0 ]
then
    echo "Error: Failed to push changes to the remote origin."
    exit 1
fi
