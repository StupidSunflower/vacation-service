FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files and fix line endings
COPY . .
RUN sed -i 's/\r$//' /code/entrypoint.sh && \
    chmod +x /code/entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]