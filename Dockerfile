FROM centos:7
ENV ENVIRONMENT_DIR=/home/odoo/.venv
ENV WORKSPACE=/home/odoo/workspace
ENV ODOO_DIR=/home/odoo/workspace/odoo
ENV INSTALLER_PATH=/home/odoo/.odoo_installer
RUN yum update
RUN yum install epel-release -y
RUN yum install centos-release-scl -y
RUN yum install rh-python36 -y
RUN yum install rh-python36-scldevel.x86_64 -y
RUN yum install rh-python36-python-devel.x86_64 -y
RUN yum install cups-devel.x86_64 -y
RUN yum install kernel-devel -y
RUN yum install vim zsh sudo git gcc wget nodejs-less libxslt-devel bzip2-devel openldap-devel libjpeg-devel freetype-devel scl-utils -y
RUN yum install gcc-c++ -y
RUN wget -P /opt/ https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.centos7.x86_64.rpm
RUN yum localinstall /opt/wkhtmltox-0.12.6-1.centos7.x86_64.rpm -y
RUN useradd -m -s /usr/bin/zsh -u 1000 odoo
COPY templates/sudoers /etc/sudoers
USER odoo
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN mkdir ${WORKSPACE}
RUN echo "source scl_source enable rh-python36" >> /home/odoo/.bashrc
RUN echo "source $ENVIRONMENT_DIR/bin/activate" >> /home/odoo/.bashrc
WORKDIR ${WORKSPACE}