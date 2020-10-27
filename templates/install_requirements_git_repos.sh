#!/bin/bash

# store the current dir
CUR_DIR=$(pwd)

# Let the person running the script know what's going on.
echo -e "\n\033[1mInstall all requirements...\033[0m\n"

# Find all git repositories and update it to the master latest revision
for i in $(find . -name "requirements.txt" | cut -c 3-); do
    echo -e "\033[33m"+$i+"\033[0m";
    pip3 install -r ./$i
done

echo  -e "\n\033[32mComplete!\033[0m\n"