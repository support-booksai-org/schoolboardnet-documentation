#!/bin/bash

cd "/Volumes/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs"

source .venv/bin/activate

mkdocs build -f mkdocs-internal.yml
