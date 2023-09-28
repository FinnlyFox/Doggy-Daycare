# Use an official Python runtime as a parent image
FROM python:latest

# Set Environment
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:8000
