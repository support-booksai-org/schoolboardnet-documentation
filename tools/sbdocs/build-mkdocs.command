#!/bin/bash
clear
cd "/Volumes/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs" || exit 1

echo "==============================================="
echo " schoolboard.net MkDocs Build + Serve"
echo "==============================================="
echo

echo "Cleaning previous build..."
rm -rf site

echo

echo "Building..."
python3 -m mkdocs build || {
  echo "Build failed."
  read -p "Press Return to close..."
  exit 1
}

echo

echo "Starting local server..."
python3 -m mkdocs serve

read -p "Press Return to close..."
