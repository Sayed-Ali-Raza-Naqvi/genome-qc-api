# Genomic Sequence Analyzer API

A FastAPI-based microservice for analyzing genomic sequences. Upload FASTA or FASTQ files to get GC content analysis, length statistics, and quality metrics powered by Biopython.

## Features

- **Sequence Format Support**: Analyze both FASTA and FASTQ files
- **GC Content Analysis**: Calculate GC content percentage for sequences
- **Quality Metrics**: Generate comprehensive quality statistics
- **RESTful API**: Simple and intuitive endpoints
- **Health Checks**: Built-in health monitoring endpoint
- **Containerized**: Docker support for easy deployment
- **Async Processing**: Efficient async request handling with FastAPI

## Tech Stack

- **Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Bioinformatics**: Biopython
- **Data Validation**: Pydantic
- **Testing**: Pytest
- **Containerization**: Docker

## Quick Start

### Prerequisites

- Python 3.8+
- Docker (optional)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd genome-qc-api
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

Access the interactive API documentation at `http://localhost:8000/docs`

## API Endpoints

### GET `/`
Welcome message and usage instructions.

### GET `/health`
Health check endpoint to verify the service is running.

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "timestamp": 1234567890
}
```

### POST `/analyze`
Upload and analyze a genomic sequence file.

**Parameters:**
- `file` (required): FASTA or FASTQ file to analyze

**Response:**
```json
{
  "filename": "example.fasta",
  "format": "fasta",
  "gc_content": 45.5,
  "metrics": { ... }
}
```

## Usage Example

```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@sample.fasta"
```

## Docker Deployment

Build the Docker image:
```bash
docker build -t genome-qc-api .
```

Run the container:
```bash
docker run -p 8000:8000 genome-qc-api
```

## Testing

Run the test suite:
```bash
pytest tests/ -v
```

## Project Structure

```
genome-qc-api/
├── app/
│   ├── main.py              # FastAPI application setup
│   ├── routes/
│   │   └── analyze.py       # API endpoints
│   ├── services/
│   │   ├── parser.py        # Sequence parsing logic
│   │   └── metrics.py       # Analysis and metrics calculation
│   ├── schemas/
│   │   └── response.py      # Pydantic response models
│   └── utils/
│       └── file_handler.py  # File handling utilities
├── tests/
│   └── test_metrics.py      # Unit tests
├── Dockerfile               # Container configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Development

### Setting Up Development Environment

1. Install development dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests before committing:
```bash
pytest tests/ -v
```

## License

This project is provided as-is for genomic sequence analysis purposes.

## Support

For issues or questions, please refer to the project documentation or contact the development team.
