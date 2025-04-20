# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js (version 16 is compatible with @openai/codex)
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Install npm (it comes with Node.js, but this ensures it's set up correctly)
RUN npm -v

# Install the @openai/codex package globally using npm
RUN npm i -g @openai/codex

# Set the working directory to /app
WORKDIR /app

# Expose port (if needed -  @openai/codex doesn't inherently use a port, but you might add a server later)
# EXPOSE 3000

# Command to run when the container starts.  By default, just open a shell.
CMD ["/bin/bash"]
