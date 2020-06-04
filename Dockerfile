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
RUN mkdir -p /opt/statewide_disaggregations/python
RUN mkdir -p /opt/statewide_disaggregations/sql_templates
COPY python/*.py /opt/statewide_disaggregations/python/
COPY sql_templates/*.* /opt/statewide_disaggregations/sql_templates/

# This will get overwritten in the Docker Compose
ADD dbconfig_template.py /opt/echoplex/dbconfig.py
WORKDIR /opt/statewide_disaggregations

ENTRYPOINT entrypoint.sh
CMD python3 --version
