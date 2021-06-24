FROM ubuntu:20.04

ENV SPARK_HOME="/opt/spark"
ENV SPARK_VERSION="2.4.0"
ENV SPARK_HADOOP_VERSION="2.7"
ENV PATH="${SPARK_HOME}/bin:${PATH}"

ENV PYSPARK_PYTHON=python2.7
ENV PATH="$SPARK_HOME/python:$PATH"

ENV JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"

WORKDIR /opt

# Setting Ubuntu default timezone
RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

# Utilities
RUN apt-get update \
    && apt-get -y install zip curl

# Java 8
RUN apt-get -y install openjdk-8-jdk

# Python 3
RUN apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python2.7 \
    && curl "https://bootstrap.pypa.io/pip/2.7/get-pip.py" --output get-pip.py \
    && python2.7 get-pip.py

ADD requirements-dev.txt .
RUN pip install -r requirements-dev.txt
RUN pip install tox

# Spark
ADD "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}.tgz" .
RUN tar -xzf spark*.tgz && rm -f spark*.tgz && mv spark* spark
RUN ln -s /opt/spark/bin/spark-submit /opt/spark/bin/spark2-submit

RUN touch /opt/spark/conf/log4j.properties
RUN echo 'log4j.rootLogger=INFO, console\n\
\n\
# Console Appender\n\
log4j.appender.console=org.apache.log4j.ConsoleAppender\n\
log4j.appender.console.layout=org.apache.log4j.PatternLayout\n\
log4j.appender.console.layout.ConversionPattern=\u001b[m%d{yyyy/MM/dd HH:mm:ss} \u001b[36;1m%p\u001b[m [\u001b[32;1m%t\u001b[m] \u001b[34;1m%c{1}\u001b[m: %m%n\n\
\n\
# Logging Level\n\
log4j.logger.org.apache=ERROR\n\
log4j.logger.org.spark_project=ERROR\n\
log4j.logger.parquet=ERROR\n' >> /opt/spark/conf/log4j.properties

WORKDIR /opt/app/
CMD tail -f /dev/null
