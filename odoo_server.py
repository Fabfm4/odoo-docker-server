#!/usr/bin/python
import sys
import os
import json
import jinja2
import subprocess

PWD_DOCKER = '/home/docker/workspace'
ODOO_EVIRONMENT_CONTAINER = 'odoo_environment2'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[32m'
    BANNER = '\033[33m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ERROR = '\033[31m'

    @staticmethod
    def print_text(color, text):
        print(getattr(bcolors, color) + text + bcolors.ENDC)


def _print_banner():
    bcolors.print_text('BANNER', "******** *****    ******** ********          ******** ******** ******** ***  *** ********* ********")
    bcolors.print_text('BANNER', "******** *****    ******** ********          ******** ******** ******** ***  *** ********* ********")
    bcolors.print_text('BANNER', "**    ** **   **  **    ** **    ** ******** ***      **       **    ** ***  *** **        **    **")
    bcolors.print_text('BANNER', "**    ** **    ** **    ** **    ** ******** ******** ******** ******** ***  *** ********* ********")
    bcolors.print_text('BANNER', "**    ** **   **  **    ** **    ** ********       ** **       ******    ******  **        ******  ")
    bcolors.print_text('BANNER', "******** ******   ******** ********          ******** ******** *** ***    ****   ********* *** *** ")
    bcolors.print_text('BANNER', "******** *****    ******** ********          ******** ******** ***  ***    **    ********* ***  ***")


def init(argv):
    bcolors.print_text("OKBLUE", "Run command init...")
    pwd = os.getcwd()
    odoo_src_path = "{0}/odoo".format(pwd)
    addons_path = "{0}/addons".format(pwd)
    config_file_json = "{0}/config.json".format(pwd)
    if argv:
        bcolors.print_text('ERROR', "Bad parameters")

    bcolors.print_text("BOLD", "Create odoo src directory...")
    if not os.path.isdir(odoo_src_path):
        os.mkdir(odoo_src_path)
        bcolors.print_text("OKGREEN", "OK...")

    else:
        bcolors.print_text("WARNING", "odoo src directory already exists")

    bcolors.print_text("BOLD", "Clone repositories in Addons path ...")
    bcolors.print_text("BOLD", "Search config.json file...")
    if os.path.exists(config_file_json):
        bcolors.print_text("BOLD", "Exists config.json file...")
        with open(config_file_json) as json_config:
            config = json.load(json_config)
            bcolors.print_text("BOLD", "Verify if git is installed ...")
            try:
                FNULL = open(os.devnull, 'w')
                subprocess.Popen("docker", stdout=FNULL, stderr=FNULL)
                FNULL.close()
                bcolors.print_text("OKGREEN", "git is already installed ... DONE!")
            except OSError:
                bcolors.print_text("ERROR", "git is not installed ... FAILED!")
                exit()

            if 'addons' in config and len('addons') > 0:
                for addon in config['addons']:
                    try:
                        subprocess.check_output(
                            [
                                'git',
                                'clone',
                                str(addon['repo']),
                                str("/".join([addons_path, addon['name_directory']]))
                            ]
                        )
                        bcolors.print_text("OKGREEN", "repo {0} cloning in {1} ... DONE!".format(addon['repo'], addon['name_directory']))
                    except Exception:
                        bcolors.print_text("ERROR", "repo {0} cloning in {1} ... FAILED!".format(addon['repo'], addon['name_directory']))
                        pass

    bcolors.print_text("BOLD", "Verify if docker is installed ...")
    try:
        FNULL = open(os.devnull, 'w')
        subprocess.Popen("docker", stdout=FNULL, stderr=FNULL)
        FNULL.close()
        bcolors.print_text("OKGREEN", "docker is already installed ... DONE!")
    except OSError:
        bcolors.print_text("ERROR", "docker is not installed ... FAILED!")
        bcolors.print_text("OKBLUE", "Install docker --> https://docs.docker.com/v17.12/install/")
        exit()

    bcolors.print_text("BOLD", "Verify if docker-compose is installed ...")
    try:
        FNULL = open(os.devnull, 'w')
        subprocess.Popen("docker-compose", stdout=FNULL, stderr=FNULL)
        FNULL.close()
        bcolors.print_text("OKGREEN", "docker-compose is already installed ... DONE!")
    except OSError:
        bcolors.print_text("ERROR", "docker-compose is not installed ... FAILED!")
        bcolors.print_text("OKBLUE", "Install docker compose --> https://docs.docker.com/compose/install/")
        exit()
    bcolors.print_text("BOLD", "Build containers...")
    try:
        subprocess.check_output(['docker-compose', 'up', '-d'])
    except Exception:
        bcolors.print_text("ERROR", "Can't build containers")

    bcolors.print_text("BOLD", "Install requirements ...")
    if os.path.exists(config_file_json):
        with open(config_file_json) as json_config:
            config = json.load(json_config)
            if 'addons' in config and len('addons') > 0:
                for addon in config['addons']:
                    if os.path.exists("{0}/{1}/requirements.txt".format(addons_path, addon['name_directory'])):
                        subprocess.check_call(
                            'docker exec -it {0} bash -c "pip3 install -r {1}/addons/{2}/requirements.txt"'.format(
                                ODOO_EVIRONMENT_CONTAINER,
                                PWD_DOCKER,
                                addon['name_directory']
                            ), shell=True
                        )

    bcolors.print_text("OKGREEN", "all requirements are installed ... DONE!")


def main(argv):
    _print_banner()
    if not argv:
        bcolors.print_text('ERROR', "Wrong Option")
        return False

    globals()[argv[0]](argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])
