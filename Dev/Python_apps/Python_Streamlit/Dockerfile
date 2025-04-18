FROM python:3.10

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install production dependencies.
RUN pip install -r requirements.txt

EXPOSE 8501

#CMD python ./app/app.py

#ENTRYPOINT ["streamlit", "run", "st_test.py", "--server.port=8501", "--server.address=0.0.0.0"]