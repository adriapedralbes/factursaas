FROM python:3.11

WORKDIR /code

# Copy requirements file
COPY ./requirements.txt /code/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code
COPY ./app /code/app

# Run the FastAPI application
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]