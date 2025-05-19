# Use nodejs 20.12.2 as base image
FROM node:20.12.2

# Display Node.js and npm versions
RUN node -v && npm -v

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install Strapi CLI globally
#RUN npm install --global create-strapi-app
RUN yes | npm install --global create-strapi-app

# Create Strapi app
#RUN npx create-strapi-app@latest my-project --quickstart
#RUN echo -ne '\n' | npx create-strapi-app@latest my-project --quickstart
#RUN expect -c 'spawn npx create-strapi-app@latest my-project --quickstart; expect "?>"; send "\r"; interact'

# Copy the script for creating Strapi app
#COPY create_strapi_app.sh /

# Run the script to create Strapi app
#RUN chmod +x /create_strapi_app.sh && /create_strapi_app.sh


# Set working directory
#WORKDIR /my-project

# Install dependencies
#RUN npm install

# Expose Strapi default port
EXPOSE 1337

# Start Strapi app
#CMD ["npm", "run", "develop"]

#docker build -t my-strapi-app_v2 .
#docker run -p 1337:1337 my-strapi-app



# FROM node:18-alpine
# # Installing libvips-dev for sharp Compatibility
# RUN apk update && apk add --no-cache build-base gcc autoconf automake zlib-dev libpng-dev nasm bash vips-dev git
# ARG NODE_ENV=development
# ENV NODE_ENV=${NODE_ENV}

# WORKDIR /opt/
# COPY package.json yarn.lock ./
# RUN yarn global add node-gyp
# RUN yarn config set network-timeout 600000 -g && yarn install
# ENV PATH /opt/node_modules/.bin:$PATH

# WORKDIR /opt/app
# COPY . .
# RUN chown -R node:node /opt/app
# USER node
# RUN ["yarn", "build"]
# EXPOSE 1337
# CMD ["yarn", "develop"]