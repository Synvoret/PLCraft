#!/bin/bash
# set -e  # Stop the script on the first error

# Set the main project directory (one level up from scripts/)
PROJECT_DIR="$(dirname "$0")/.."
cd "$PROJECT_DIR" || exit

# Remove __pycache__ directories and .pyc files
echo "🗑 Removing __pycache__ directories and .pyc files..."
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
echo "✅ Done!"

# Sort and organize imports using isort
echo "📦 Running isort - organizing imports"
isort "$PROJECT_DIR"

# Format Python code using Black
echo "🎨 Running Black - formatting code"
black "$PROJECT_DIR"

# Check code style and unused imports using Flake8
echo "🔍 Running Flake8 - checking code style and unused imports"
flake8 "$PROJECT_DIR" || true  # Do not stop the script if linting fails


# Remove unused imports and variables (ignore __init__.py)
echo "🧹 Running autoflake - removing unused imports and variables"
autoflake --remove-unused-variables \
          --recursive --ignore-init-module-imports --in-place --exclude venv "$PROJECT_DIR"

# Check and reformat Django templates using djlint
echo "🧪 Running djlint - fixing Django templates"
djlint "$PROJECT_DIR" --reformat

echo "✅ All checks and cleanups completed successfully!"