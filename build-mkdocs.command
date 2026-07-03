#!/bin/bash
clear

cd "/Volumes/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs" || exit 1

echo "Cleaning previous build..."
rm -rf site

echo
echo "Building..."
python3 -m mkdocs build

echo
echo "Starting local server..."
python3 -m mkdocs serve

read -p "Press Return to close..."