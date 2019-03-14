FROM ubuntu:18.04

RUN mkdir -p /odoo/workspace/addons
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install git python3-pip build-essential \
    wget python3-dev python3-venv python3-wheel libpq-dev \
    libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less -y
RUN pip3 install Babel decorator docutils ebaysdk feedparser gevent greenlet html2text
RUN pip3 install Jinja2 lxml Mako MarkupSafe mock num2words ofxparse passlib Pillow
RUN pip3 install psutil psycogreen psycopg2 pydot pyparsing PyPDF2 pyserial
RUN pip3 install python-dateutil python-openid pytz pyusb PyYAML qrcode reportlab
RUN pip3 install requests six suds-jurko vatnumber vobject Werkzeug XlsxWriter xlwt xlrd
RUN apt-get install -y npm
RUN npm install -g less less-plugin-clean-css
RUN apt-get install node-less
RUN python3 -m pip install libsass
RUN git clone https://www.github.com/odoo/odoo --depth 1 --branch 12.0 --single-branch /odoo/workspace/odoo
RUN pip3 install -r /odoo/workspace/odoo/requirements.txt
RUN apt-get update
RUN apt-get install -y wkhtmltopdf xvfb
RUN pip3 install pyOpenSSL
WORKDIR /odoo/workspace
