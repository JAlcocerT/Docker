FROM python:3.11

# Install git
RUN apt-get update && apt-get install -y git

# Set up the working directory
WORKDIR /app

# Clone the repository
RUN git clone --depth=1 https://github.com/phidatahq/phidata && \
    cd phidata && \
    git sparse-checkout init && \
    git sparse-checkout set cookbook/llms/groq/video_summary && \
    git pull origin main

#RUN sed -i 's/numpy==1\.26\.4/numpy==1.24.4/; s/pandas==2\.2\.2/pandas==2.0.2/' requirements.txt


# Set the entrypoint to a bash shell
CMD ["/bin/bash"]
