# Use the Alpine version of the official Nginx image
FROM nginx:alpine

# Install required packages
RUN apk add --no-cache nginx-mod-http-dav-ext apache2-utils

# Create a directory for WebDAV files
RUN mkdir /media && chown nginx:nginx /media

# Add configuration file for Nginx
COPY webdav.conf /etc/nginx/conf.d/default.conf

# Remove default server definitions
RUN rm /etc/nginx/conf.d/default.conf

# Copy the WebDAV specific configuration to Nginx
COPY webdav.conf /etc/nginx/conf.d/

# Copy the entrypoint script to the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose port 80
EXPOSE 80

# Volume for WebDAV files
VOLUME /media

# Command to run the entrypoint script and start Nginx in the foreground
CMD ["/entrypoint.sh"]


### docker build -t my-webdav-server .