# Use a lightweight Python base image
FROM python:3.11-slim
# Set working directory inside the container
WORKDIR /app

# Install OS dependencies for common Python libs (safe set)
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Expose the port the app runs on
EXPOSE 5000
# Command to run the application
CMD ["python", "app.py"]


