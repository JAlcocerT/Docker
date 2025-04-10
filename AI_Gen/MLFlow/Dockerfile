# Use the specified Python base image
FROM python:3.10.12-slim 
#https://hub.docker.com/_/python/tags?name=3.10.12

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# Install production dependencies.
RUN pip install -r requirements.txt



# Keep the container running
#CMD ["tail", "-f", "/dev/null"]


#docker build -t mlflow .