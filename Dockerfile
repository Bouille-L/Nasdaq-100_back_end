# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Add Gunicorn to your requirements.txt or install it here directly
RUN pip install gunicorn

# Expose the port your app runs on (not necessary for Heroku, but good practice)
EXPOSE $PORT

# Command to run the application using Gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT --workers 4 Nasdaq_100_ETF_Explorer.wsgi:application

