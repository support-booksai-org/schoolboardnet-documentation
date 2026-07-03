#!/bin/bash

clear

echo "==============================================="
echo " schoolboard.net Documentation Build"
echo "==============================================="
echo

# Change to your sbDocs folder
cd "/Volumes/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/tools/sbdocs" || {
    echo "ERROR: Cannot find sbDocs folder."
    read -p "Press Return to exit..."
    exit 1
}

echo "Current Directory:"
pwd
echo

echo "Building documentation..."
echo

python3 sbdocs.py

echo
echo "==============================================="
echo "Build complete."
echo "==============================================="
echo

read -p "Press Return to close..."