FROM ubuntu:18.10

ENV DEBIAN_FRONTEND noninteractive

# Install the basics
RUN apt-get clean && apt-get update \
    && apt-get install -y python3-pip gdal-bin python3-pyproj \
    build-essential wget ca-certificates postgresql postgresql-contrib \
    postgis

ADD requirements.txt /tmp/
ADD entrypoint.sh /usr/local/bin/

# Install PIP requirements
RUN pip3 install -r /tmp/requirements.txt

# Set up our run environment
RUN mkdir -p /opt/echoplex
COPY python/*.py /opt/echoplex/
COPY sql_templates/*.* /opt/echoplex/

# This will get overwritten in the Docker Compose
ADD dbconfig_template.py /opt/echoplex/dbconfig.py
WORKDIR /opt/echoplex

ENTRYPOINT entrypoint.sh
CMD python3 --version
