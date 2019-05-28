#!/bin/bash
ODOO_DIRECTORY=$(pwd)/odoo

echo -e "\n\033[1mInit Project...\033[0m\n"

echo -e "\033[33mCreate odoo directory\033[0m";
if [ ! -d "$ODOO_DIRECTORY" ]; then
    mkdir $ODOO_DIRECTORY
    echo -e "\033[32mOK...\033[0m";
else
    echo -e "\033[31mDirectory odoo already exists\033[0m";
fi
