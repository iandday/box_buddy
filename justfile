# Set the default shell for commands
set shell := ["bash", "-c"]


css:
    @echo "Watching and rebuilding CSS"
    ./tailwindcss-extra -i box_buddy/static/css/input.css -o box_buddy/static/css/output.css --watch

dev:
    @echo "Starting django server"
    uv run manage.py runserver_plus

up:
    @echo "Starting docker containers"
    docker compose up --watch

rebuild:
    @echo "Rebuilding the Docker containers..."
    docker compose up --watch rebuild

# view rendered mkdocs
mkdocs:
    uv run mkdocs serve -a localhost:8001


lint:
    @echo "Running Ruff linter"
    uv run ruff check .


format:
    @echo "Formatting code with Ruff"
    uv run ruff format



pre-commit:
    @echo "Running pre-commit hooks..."
    uv run pre-commit run --all-files

# Make migrations
makemigrations:
    @echo "Running Django makemigrations..."
    uv run python manage.py makemigrations

# Run migrations
migrate:
    @echo "Running Django migrations..."
    uv run python manage.py migrate

# Collect static files
collectstatic:
    @echo "Collecting static files..."
    uv run python manage.py collectstatic --noinput
#------



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



# Create a superuser
superuser:
    @echo "Creating a Django superuser..."
    python manage.py createsuperuser



# Clean up Docker containers and images
docker-clean:
    @echo "Cleaning up Docker containers and images..."
    docker system prune -af

# Install dependencies
install:
    @echo "Installing dependencies..."
    pip install -r requirements.txt
