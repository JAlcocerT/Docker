# Use an official Node runtime as the parent image - https://hub.docker.com/_/node/
FROM node:20.12.2-bullseye 
# 18.19-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json (if available) into the container
#COPY package*.json ./


RUN git clone http://192.168.3.200:3033/fossengineer/CyclingThere2 .


#WORKDIR /usr/src/app/CyclingThere2/pacamara
# Install any dependencies
#RUN npm install

# Copy the rest of your app's source code into the container
#COPY . .

# Build your Astro project
#RUN npm run build

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 4321

# Define the command to run your app using CMD which defines your runtime
#CMD [ "npm", "start" ]




### docker build -t astro_ssg -f Dockerfile .