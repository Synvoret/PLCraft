#!/bin/bash

# Format code using black
echo "🎨 black - formatting code"
black .

# Check code style and unused imports using flake8
echo "🔍 flake8 - checking code style and unused imports"
flake8 .

# Sort and organize imports using isort
echo "📦 isort - organizing imports"
isort . --check-only

# Remove unused imports using autoflake
echo "🧹 autoflake - removing unused imports"
autoflake --remove-all-unused-imports --recursive --ignore-init-module-imports --exclude venv .

# Check Django templates using djlint
echo "🧪 djlint - checking Django templates"
djlint templates/ --check

# to run this script, use:
# bash backend/check_project.sh