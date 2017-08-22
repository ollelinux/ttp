# Start with a Python image
FROM python:latest

# File maintainer
MAINTAINER olle

# Ensure that Python outputs everything that's printed 
# inside the application rather than buffering it
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE config.docker_settings

# Copy all files into the image
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install requirements
RUN pip install -U pip
RUN pip install -Ur requirements.txt

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# Specify the command to run when the image is run
# CMD ["python"]
