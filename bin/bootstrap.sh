#!/bin/bash

# Check if npm is installed
npm --version >/dev/null 2>&1
if [ $? -ne 0 ]
then
    echo "Installing npm..."
    
    # Check if the nvm is installed
    nvm --version >/dev/null 2>&1
    if [ $? -ne 0 ]
    then
        echo "Error: nvm is not installed"
        echo "Try: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash"
        echo "Search for the latest nvm instead of 0.38.0"
        exit 1
    fi

    # Install the latest npm LTS with the nvm
    nvm install --lts
fi

# Install Eleventy
eleventy --version >/dev/null 2>&1
if [ $? -ne 0 ]
then
    echo "Installing Eleventy..."
    npm install @11ty/eleventy -g
fi

# Install Marp
npx marp --version >/dev/null 2>&1
if [ $? -ne 0 ]
then
    echo "Installing Marp..."
    npm install --save-dev @marp-team/marp-cli
fi

# Install the local dependencies
echo "Installing dependencies..."
npm install

# Compile a first time the website (to make sure all dependencies are fine)
echo "Compiling..."
npm run -s build