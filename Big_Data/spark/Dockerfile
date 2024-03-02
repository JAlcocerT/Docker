FROM openjdk:8-jdk

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pyspark

# Download and install Spark - https://downloads.apache.org/spark/
ARG SPARK_VERSION=3.4.2
ARG HADOOP_VERSION=3
RUN curl -sL --retry 3 \
  "https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" \
  | gunzip \
  | tar x -C / && \
  mv /spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /spark

# Set environment variables
ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYSPARK_PYTHON=python3

WORKDIR $SPARK_HOME


# docker build -t my-pyspark-image .
#docker run -it --name pyspark-shell my-pyspark-image /bin/bash
#python3 --version