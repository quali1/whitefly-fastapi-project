# Whitefly FastAPI Project

## Setup

1. **Build and run the containers:**

    ```bash
    docker-compose up --build
    ```

2. **Access the application:**

    The FastAPI application will be running at `http://localhost:8000`.

## Usage

- **Home Page:**
  Access the home page at `http://localhost:8000` to interact with the API.

- **Regular Form:**
  Submit a form to add a user synchronously.

- **Async Form:**
  Submit a form to add a user asynchronously using Celery.

## Adding a New User Synchronously

1. Navigate to `http://localhost:8000/regular_form`
2. Fill out the form and submit.

## Adding a New User Asynchronously

1. Navigate to `http://localhost:8000/async_form`
2. Fill out the form and submit.

## Project Structure

- **app/__init__.py:** Initializes the FastAPI app.
- **app/config.py:** Configuration for the FastAPI app.
- **app/main.py:** Entry point for the FastAPI app, sets up routes and other settings.
- **app/models.py:** Contains the database models.
- **app/routers.py:** Defines the API routes.
- **app/services.py:** Contains the business logic and service functions.
- **requirements.txt:** List of dependencies to be installed.

## Stopping the Containers

To stop the containers, run:

```bash
docker-compose down
