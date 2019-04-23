FROM ubuntu:18.10

RUN mkdir -p /odoo/workspace/addons
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install python3.7 -y
RUN apt-get install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less gcc musl-dev -y
RUN pip3 install Babel decorator docutils ebaysdk feedparser gevent greenlet html2text Jinja2 lxml Mako MarkupSafe mock num2words ofxparse passlib Pillow psutil psycogreen psycopg2-binary pydot pyparsing PyPDF2 pyserial python-dateutil python-openid pytz pyusb PyYAML qrcode reportlab requests six suds-jurko vatnumber vobject Werkzeug XlsxWriter xlwt xlrd
RUN apt-get install -y npm
RUN npm i npm@latest -g
RUN npm install -g less less-plugin-clean-css
RUN apt-get install node-less
RUN python3 -m pip install libsass
RUN git clone https://www.github.com/odoo/odoo --depth 1 --branch 12.0 --single-branch /odoo/workspace/odoo
RUN pip3 install -r /odoo/workspace/odoo/requirements.txt
RUN apt-get update
RUN apt-get install -y wkhtmltopdf xvfb
RUN wget https://builds.wkhtmltopdf.org/0.12.1.3/wkhtmltox_0.12.1.3-1~bionic_amd64.deb
RUN apt install ./wkhtmltox_0.12.1.3-1~bionic_amd64.deb -y
RUN cp /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage
RUN cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf
RUN pip3 install pyOpenSSL
WORKDIR /odoo/workspace
ADD addons /odoo/workspace/addons
RUN find "$PWD" -name requirements.txt -exec pip3 install -r {} \;
RUN cd /odoo/workspace/odoo && python3.6 setup.py install
RUN pip3 install inotify
RUN apt-get install -y postgresql-client
