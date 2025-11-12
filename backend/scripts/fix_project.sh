#!/bin/bash

# set main path (one level up from scripts/)
PROJECT_DIR="$(dirname "$0")/.."
cd "$PROJECT_DIR" || exit


# Format code using black
echo "🎨 black - formatting code"
black "$PROJECT_DIR"

# Check code style and unused imports using flake8
echo "🔍 flake8 - checking code style and unused imports"
flake8 "$PROJECT_DIR"

# Sort and organize imports using isort
echo "📦 isort - organizing imports"
isort "$PROJECT_DIR" --check-only

# Remove unused imports using autoflake
echo "🧹 autoflake - removing unused imports"
autoflake --remove-all-unused-imports --recursive --ignore-init-module-imports --exclude venv "$PROJECT_DIR"

# Check Django templates using djlint
echo "🧪 djlint - checking Django templates"
djlint templates/ --check

# to run this script, use:
# bash ./scripts/check_project.sh