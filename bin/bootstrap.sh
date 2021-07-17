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
        echo "Installing nvm 0.38.0..."
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
        if [ -f $HOME/.zshrc ]
        then
            echo "Updating PATH in .zshrc..."
            echo "" >> $HOME/.zshrc
            echo "# NVM 0.38.0" >> $HOME/.zshrc
            echo "export NVM_DIR=\"$HOME/.nvm\"" >> $HOME/.zshrc
            echo "[ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\"  # This loads nvm" >> $HOME/.zshrc
            echo "[ -s \"$NVM_DIR/bash_completion\" ] && \\. \"$NVM_DIR/bash_completion\"  # This loads nvm bash_completion" >> $HOME/.zshrc
        fi
        exit 1
    fi

    # Install the latest npm LTS with the nvm
    echo "Installing NPM..."
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

# Install plantuml
plantuml -h >/dev/null 2>&1s
if [ $? -ne 0 ]
then
    echo "Installing plantuml..."
    sudo apt-get install plantuml
fi