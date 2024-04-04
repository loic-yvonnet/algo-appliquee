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
        echo "Installing nvm 0.39.0..."
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
        if [ -f $HOME/.zshrc ]
        then
            echo "Updating PATH in .zshrc..."
            echo "" >> $HOME/.zshrc
            echo "# NVM 0.39.1" >> $HOME/.zshrc
            echo "export NVM_DIR=\"$HOME/.nvm\"" >> $HOME/.zshrc
            echo "[ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\"  # This loads nvm" >> $HOME/.zshrc
            echo "[ -s \"$NVM_DIR/bash_completion\" ] && \\. \"$NVM_DIR/bash_completion\"  # This loads nvm bash_completion" >> $HOME/.zshrc
        fi
        
        NVM_DIR="$HOME/.nvm"
        $NVM_DIR/nvm.sh
        $NVM_DIR/bash_completion
    fi

    # Install the latest npm LTS with the nvm
    echo "Installing NPM..."
    nvm install 18
    nvm use 18
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
if [ $? -ne 0 ]
then
    echo "Error: Failed to install the npm dependencies."
    exit 1
fi

# Compile a first time the website (to make sure all dependencies are fine)
echo "Compiling..."
npm run -s build
if [ $? -ne 0 ]
then
    echo "Error: Failed to build the project."
    exit 1
fi

# Install plantuml
plantuml -h >/dev/null 2>&1
if [ $? -ne 0 ]
then
    # Debian-based distro
    which apt-get >/dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "Installing plantuml..."
        sudo apt-get install plantuml
    fi

    # Brew on macOS
    which brew >/dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "Installing plantuml..."
        brew install plantuml
    fi
fi