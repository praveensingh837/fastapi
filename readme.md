# Incident Manager API

This project is a simple FastAPI application for managing incident records. It uses SQLAlchemy with SQLite and creates the database automatically when the app starts.

## Project structure

```bash
fastapi/
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       └── incidents.py
├── incident_manage.db
├── requirment.txt
└── readme.md
```

## Features

- FastAPI application setup
- SQLite database connection
- SQLAlchemy models for incidents
- Automatic table creation on startup
- Root endpoint for health check

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.9+
- pip
- virtual environment support

## Setup steps

1. Open a terminal and go to the project folder:

```bash
cd fastapi
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install fastapi uvicorn sqlalchemy
```

> Note: the current file named `requirment.txt` is empty, so the dependencies above are the ones required by the code in this project.

## Run the application

From the project root, start the FastAPI server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

If you prefer to run it with Python directly:

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Access the API

Once the app is running, open:

- API homepage: http://127.0.0.1:8000/
- Swagger docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Root endpoint

The app currently exposes a simple health-check endpoint in `app/main.py`:

```json
{"message": "Incident manager app is running."}
```

## Database

The application uses SQLite and creates the database file automatically:

```bash
incident_manage.db
```

This file is created in the project root when the app starts.

## Notes

- `app/routers/incidents.py` and `app/schemas.py` exist but are currently empty, so the API does not yet have CRUD routes implemented.
- The app is ready for extension with incident create, read, update, and delete endpoints.
