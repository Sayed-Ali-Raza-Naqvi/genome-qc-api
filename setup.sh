#!/bin/bash

# Create main directories
mkdir -p app/routes
mkdir -p app/services
mkdir -p app/schemas
mkdir -p app/utils
mkdir -p tests
mkdir -p data
mkdir -p notebooks

# Create files
touch app/main.py
touch app/routes/analyze.py
touch app/services/parser.py
touch app/services/metrics.py
touch app/schemas/response.py
touch app/utils/file_handler.py

touch tests/test_parser.py
touch tests/test_metrics.py
touch tests/test_routes.py

touch data/sample.fasta

touch notebooks/genome_qc_analysis.ipynb

touch Dockerfile
touch requirements.txt
touch .dockerignore
touch README.md
/.gitignore

# Add basic .gitignore content
cat <<EOL > .gitignore
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.DS_Store
*.log
EOL

echo "Project structure for genome-qc-api created successfully!"