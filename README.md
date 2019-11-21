# Odoo Server Docker
This project is to manage a environment where you can develop your [ODOO](https://www.odoo.com/es_ES/) application


### What do you need?

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Python](python.org)


#### Steps

1. You should clone this repo in any folder where you want to save your project
* command:
```sh
$ git clone git@github.com:Fabfm4/odoo-docker-server.git
```

2. When it has finished you need run the next command, this is going to create new 
containers one is where the code will be and the next is where database will save
```sh
$ docker-compose up -d
```
Note: if you use ```-d``` flag your containers will be running on background

3. Now you need access to ```addons``` directory, you can find this tree:
```tree
addons/
├── application.json
├── install_application.py
├── install_requirements_git_repos.sh
└── update_git_repos.sh
```

4. THE important file is ```application.json``` is a simple json file where we save our main
project:
```json
{
    "main_repo": "<repo>",
    "main_project": "<name of project>"
}
```
in attribute ```main_repo``` we will write the ssh url from your repo
in attribute ```main_project``` we will write the name which you want to called your project. Now
when you already write those values execute the next command:
```sh
$ python install_application.py
```
NOTE: Remember in your main project must exist a file called ```oca_dependences.txt``` where you save all dependences you
need 

5. execute the next command to install all pip requirements: 
```sh
$ ./install_requirements_git_repos.sh
```

So far we installed all requirements in containers of docker. Now we need to be inside to containers:
#### How you can be inside of container

the main structure of command is:
```sh
$ docker exec -it <name_of_container> bash
```
You can see your containers which are up you need use the next command:
```sh
$ docker ps
```

In this case we need be inside of code container and execute the next commands
```sh
$ docker exec -it odoo_environment bash
...
# sh /entrypoint.sh
```

The last command will download the last version of public odoo ([repo](http://github.com/odoo/odoo))


