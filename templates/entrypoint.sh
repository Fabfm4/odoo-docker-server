#!/bin/bash
if [ ! -d $ODOO_DIR ]; then
    mkdir -p $ODOO_DIR;
fi;
if [ ! -d $ODOO_DIR/.git ]; then
    git clone https://www.github.com/odoo/odoo --depth 1 --branch 12.0 --single-branch $ODOO_DIR
else
    cd $ODOO_DIR
    git remote update
    git checkout .
    git rebase origin/12.0
fi;
pip3 install -r $ODOO_DIR/requirements.txt
chown -R docker:docker $ODOO_DIR
