#!/bin/bash
set -e

echo "Installing requirements..."
pip install -r requirements.txt

echo "Initializing Reflex..."
reflex init

echo "Exporting frontend..."
reflex export --frontend-only

echo "Build complete."
