# Use nodejs 20.12.2 as base image
FROM node:20.12.2

# Display Node.js and npm versions
RUN node -v && npm -v

# Set working directory
WORKDIR /usr/src/app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y wget git xdg-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the Hugo theme repository (changed to slidev)
RUN git clone https://github.com/JAlcocerT/slidev /slidev

# Set the working directory to the exampleSite within the cloned theme
WORKDIR /slidev/slidevsample

# Install Slidev CLI globally
RUN npm install -g @slidev/cli
#To export to PDF
RUN npm i -D playwright-chromium 
RUN npx playwright install-deps


# Expose port 3030 for SliDevJS
EXPOSE 3030

# Start Slidev in development mode
#CMD ["slidev", "--open"]

#docker build -t slidev_ppt .
#docker run -d -p 3030:3030 --name slidev_instance --restart unless-stopped slidev_ppt
#docker exec -it slidev_instance /bin/bash

# # Use nodejs 20.12.2 as base image
# FROM node:20.12.2

# # Display Node.js and npm versions
# RUN node -v && npm -v

# # Set working directory
# WORKDIR /usr/src/app

# # Install Hugo for Hextra
# RUN apt-get update && \
#     apt-get install -y wget && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # Clone the Hugo theme repository
# RUN git clone https://github.com/JAlcocerT/slidev /slidev

# # Set the working directory to the exampleSite within the cloned theme
# WORKDIR /slidev/slidevsample 

# RUN npm install -g @slidev/cli #npm install --save-dev @slidev/cli


# # Expose port 300 for SliDevJS
# EXPOSE 3030

# #docker build -t slidev_ppt .
# #docker run -d -p 3030:3030 --name slidev_instance --restart unless-stopped slidev_ppt tail -f /dev/null
# #docker exec -it slidev_instance /bin/bash
# #go version
# #hugo version