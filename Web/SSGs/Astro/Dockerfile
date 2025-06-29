#https://hub.docker.com/_/node
# Stage 1: Build the Astro site
FROM node:22.16-alpine3.22 as builder
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the source code
COPY . .

# Build the Astro site
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy the built site from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom nginx config if needed
# COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]


# # Use an official Node runtime as the parent image - https://hub.docker.com/_/node/
# FROM node:20.12.2-bullseye 
# # 18.19-alpine

# # Set the working directory in the container
# WORKDIR /usr/src/app

# # Copy the package.json and package-lock.json (if available) into the container
# #COPY package*.json ./


# RUN git clone http://192.168.3.200:3033/fossengineer/CyclingThere2 .


# #WORKDIR /usr/src/app/CyclingThere2/pacamara
# # Install any dependencies
# #RUN npm install

# # Copy the rest of your app's source code into the container
# #COPY . .

# # Build your Astro project
# #RUN npm run build

# # Inform Docker that the container is listening on the specified port at runtime.
# EXPOSE 4321

# # Define the command to run your app using CMD which defines your runtime
# #CMD [ "npm", "start" ]




# ### docker build -t astro_ssg -f Dockerfile .