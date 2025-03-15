# Use the official Golang image which is based on Debian Bullseye
FROM golang:1.23.2-bullseye 
#https://hub.docker.com/_/golang/tags

# Set working directory
WORKDIR /usr/src/app

# Install Hugo for Hextra
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/gohugoio/hugo/releases/download/v0.121.2/hugo_0.121.2_linux-arm64.deb && \
    dpkg -i hugo_0.121.2_linux-arm64.deb && \
    rm hugo_0.121.2_linux-arm64.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the Hugo theme repository
RUN git clone https://github.com/nicokaiser/hugo-theme-gallery /hugo-theme-gallery

# Set the working directory to the exampleSite within the cloned theme
WORKDIR /hugo-theme-gallery/exampleSite

# Expose port 1319 for Hugo server
EXPOSE 1319

# Start Hugo server
CMD ["hugo", "server", "--bind=0.0.0.0", "--baseURL=http://192.168.0.117", "--port=1319"]

#docker build -t hugo_gallery .
#docker run -d -p 1319:1319 --name hugo_gallery_instance --restart unless-stopped hugo_gallery tail -f /dev/null
#docker exec -it hugo_gallery_instance /bin/bash
#go version
#hugo version