# Set the default shell for commands
set shell := ["bash", "-c"]

# view rendered mkdocs
mkdocs:
    uv run mkdocs serve

# Run linting using Ruff
lint:
    @echo "Running Ruff linter..."
    uv run ruff check .

# Format code using Black
format:
    @echo "Formatting code with Ruff"
    uv run ruff format

#------

# Run the Django development server
dev:
    @echo "Starting the Django development server..."
    uvicorn box_buddy.asgi:application --reload --host 0.0.0.0 --port 8000

# Run tests using pytest
test:
    @echo "Running tests..."
    pytest

# Build the Docker image
docker-build:
    @echo "Building the Docker image..."
    docker build -t box_buddy .

# Run the Docker container
docker-run:
    @echo "Running the Docker container..."
    docker run --rm -it -p 8000:8000 box_buddy

# Run migrations
migrate:
    @echo "Running Django migrations..."
    python manage.py migrate

# Create a superuser
superuser:
    @echo "Creating a Django superuser..."
    python manage.py createsuperuser

# Collect static files
collect-static:
    @echo "Collecting static files..."
    python manage.py collectstatic --noinput

# Clean up Docker containers and images
docker-clean:
    @echo "Cleaning up Docker containers and images..."
    docker system prune -af

# Install dependencies
install:
    @echo "Installing dependencies..."
    pip install -r requirements.txt

# Run pre-commit hooks
pre-commit:
    @echo "Running pre-commit hooks..."
    pre-commit run --all-files
