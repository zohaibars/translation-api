#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install IndicTransTokenizer
echo "Cloning IndicTransTokenizer..."
git clone https://github.com/VarunGumma/IndicTransTokenizer || { echo "Failed to clone repository"; exit 1; }
cd IndicTransTokenizer
echo "Installing IndicTransTokenizer..."
pip install --editable ./ || { echo "Failed to install IndicTransTokenizer"; exit 1; }

echo "IndicTransTokenizer installed successfully."
