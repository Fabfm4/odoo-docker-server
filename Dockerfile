FROM ubuntu:18.04

ENV DOCKER_USER "docker"
ENV DOCKER_USER_ID "1000"
ENV PROJECT_PATH /home/docker
ENV ODOO_DIR /home/docker/workspace/odoo

RUN useradd -u ${DOCKER_USER_ID} -mU ${DOCKER_USER}


RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install git libcups2-dev -y
RUN apt-get install python3.7 -y
RUN apt-get install python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less gcc musl-dev libpq-dev -y
RUN pip3 install Babel decorator docutils ebaysdk feedparser gevent greenlet html2text Jinja2 lxml Mako MarkupSafe mock num2words ofxparse passlib Pillow psutil psycogreen psycopg2-binary pydot pyparsing PyPDF2 pyserial python-dateutil python-openid pytz pyusb PyYAML qrcode reportlab requests six suds-jurko vatnumber vobject Werkzeug XlsxWriter xlwt xlrd
RUN python3 -m pip install libsass
RUN apt-get update
RUN apt-get install -y wkhtmltopdf xvfb
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.1.4-2/wkhtmltox_0.12.1.4-2.bionic_amd64.deb
RUN apt install ./wkhtmltox_0.12.1.4-2.bionic_amd64.deb -y
RUN cp /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage
RUN cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf
RUN pip3 install --upgrade pip
RUN pip3 install pyOpenSSL
WORKDIR ${PROJECT_PATH}/workspace
RUN pip3 install inotify
RUN apt-get install -y postgresql-client
COPY templates/entrypoint.sh /
