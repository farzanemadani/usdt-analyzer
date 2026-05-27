# USDT Analyzer Backend

USDT Analyzer is a Django + Django REST Framework backend for tracking the USDT price, storing snapshots over time, and exposing simple API endpoints for a frontend dashboard.

The frontend has been deployed on Vercel:
https://usdt-analyzer-next-app.vercel.app/

## Features

- Fetches the latest USDT price and 24h volume from CoinGecko
- Stores historical price records in the database
- Calculates price deviation from the $1 peg
- Labels market status as `normal`, `warning`, or `bubble`
- Exposes REST API endpoints for charts and status widgets
- Runs a background scheduler to collect fresh data every minute
- Removes records older than 24 hours once per day

## Tech Stack

- Python
- Django
- Django REST Framework
- APScheduler
- Requests
- SQLite for local development
- PostgreSQL-compatible setup via `DATABASE_URL` in production

## API Endpoints

Base path: `/api/`

- `GET /api/prices/`  
  Returns the most recent saved price records.

- `GET /api/fetch/`  
  Fetches the current USDT price from CoinGecko and saves it immediately.

- `GET /api/status/`  
  Returns the latest market snapshot including price, volume, deviation, status, and timestamp.

## Data Model

Each `USDTPrice` record stores:

- `exchange`
- `price`
- `volume_24h`
- `created_at`

Computed fields:

- `deviation`: percentage distance from `$1.00`
- `bubble_status`: `normal`, `warning`, or `bubble`

## Local Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the required settings:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

Optional:

```env
DATABASE_URL=postgres://...
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/api/
```

## Background Jobs

The scheduler starts when the Django app is loaded.

- Every 1 minute: fetch and save the latest USDT price
- Every day at 03:00: delete records older than 24 hours

## Production Notes

- Static files are served with WhiteNoise
- CORS is enabled for cross-origin frontend access
- The project includes `Procfile` and `start.sh` for deployment workflows

## Project Structure

```text
config/     Django project settings and URLs
tracker/    Core app for models, API views, services, and scheduler
manage.py   Django management entry point
```
