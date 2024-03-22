# Use an official Node runtime as the parent image
FROM node:18.19-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json (if available) into the container
#COPY package*.json ./

# Install any dependencies
RUN npm install

# Copy the rest of your app's source code into the container
COPY . .

# Build your Astro project
RUN npm run build

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 3000

# Define the command to run your app using CMD which defines your runtime
#CMD [ "npm", "start" ]




### docker build -t astro_ssg -f Dockerfile .