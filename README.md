# Predictive Analytics API

A Flask-based REST API that periodically collects data, generates predictive models, and serves predictions through API endpoints.

## Features

- Automated data collection and model training via scheduled jobs
- REST API endpoints for accessing prediction results
- SQLAlchemy database integration for storing predictions
- APScheduler integration for periodic tasks

## Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)
- Git

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a conda environment:
```bash
conda create -n madden-env python=3.11 -y
```

3. Activate the environment:
```bash
conda activate madden-env
```

4. Install core dependencies via conda:
```bash
conda install numpy pandas -y
```

5. Install additional dependencies via pip:
```bash
pip install nfl-data-py
# Add other pip dependencies as needed
```

## Configuration

Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=sqlite:///app.db  # or your database URL
SECRET_KEY=your-secret-key
```

## Running the Application

1. **Activate the conda environment** (if not already activated):
```bash
conda activate madden-env
```

2. **Run in development mode**:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

### Verify Installation

To verify that `nfl-data-py` and dependencies are installed correctly:
```bash
python tools/test_nfl_data.py
```

## API Endpoints

Documentation for API endpoints will be added as they are implemented.

## Project Structure

```
project/
├── app/
│   ├── __init__.py          # Application factory and extensions
│   ├── models/              # Database models
│   ├── routes/              # API endpoints
│   ├── services/            # Business logic and data processing
│   └── scheduler/           # Scheduled job definitions
├── tools/                   # Developer utilities (not included in builds)
│   ├── test_nfl_data.py     # Test nfl-data-py installation
│   ├── export_requirements.py  # Export conda env to requirements.txt
│   └── README.md            # Tools documentation
├── config.py                # Configuration settings
├── requirements.txt         # Project dependencies (generated)
├── Dockerfile.example       # Sample Docker configuration
└── run.py                   # Application entry point
```

## Developer Tools

The `tools/` directory contains utilities for local development:

- **`test_nfl_data.py`** - Verify nfl-data-py installation
- **`export_requirements.py`** - Generate requirements.txt for containerization

See [tools/README.md](tools/README.md) for detailed documentation.

## Containerization

To containerize this application:

1. Export requirements:
```bash
python tools/export_requirements.py
```

2. Rename and customize the Dockerfile:
```bash
mv Dockerfile.example Dockerfile
```

3. Build and run:
```bash
docker build -t madden-api .
docker run -p 5000:5000 madden-api
```

See [tools/README.md](tools/README.md) for more details.

## License

[Your chosen license] 