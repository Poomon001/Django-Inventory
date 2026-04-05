# Use official Python image as the base image
FROM python:3.11-alpine

# output of the commands in the terminal immediately 
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container called 'app'
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# install the dependencies described in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will run on
EXPOSE 8000