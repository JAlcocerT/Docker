# Use the specified Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    build-essential

# Clone the private repository
RUN git clone https://github.com/imartinez/privateGPT

WORKDIR /app/privateGPT

# Install poetry
RUN pip install poetry

# Copy the project files into the container
COPY . /app

#Adding openai pre v1 to avoid error
RUN sed -i '/\[tool\.poetry\.dependencies\]/a openai="0.28.1"' pyproject.toml

# Lock and install dependencies using poetry
RUN poetry lock
RUN poetry install --with ui,local

# Run setup script
#RUN poetry run python scripts/setup # download models

# Keep the container running
#CMD ["tail", "-f", "/dev/null"]


#docker build -t privategpt .
#docker tag py_gpt4all docker.io/fossengineer/privategpt:v1
#docker push docker.io/fossengineer/privategpt:v1