#!/usr/bin/python
import sys
import os
import json
from subprocess import Popen, PIPE


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
    bcolors.print_text('BANNER', "******** *****    ******** ********          ******** ******** ********")
    bcolors.print_text('BANNER', "******** *****    ******** ********          ******** ******** ********")
    bcolors.print_text('BANNER', "**    ** **   **  **    ** **    ** ******** ***      **       **    **")
    bcolors.print_text('BANNER', "**    ** **    ** **    ** **    ** ******** ******** ******** ********")
    bcolors.print_text('BANNER', "**    ** **   **  **    ** **    ** ********       ** **       ******")
    bcolors.print_text('BANNER', "******** ******   ******** ********          ******** ******** *** ***")
    bcolors.print_text('BANNER', "******** *****    ******** ********          ******** ******** ***  ***")


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
            if 'addons' in config and len('addons') > 0:
                for addon in config['addons']:
                    pipe = Popen('git clone {0} {1}/{2}'.format(
                        addon['repo'], addons_path, addon['name_directory']
                    ), shell=True, stdout=PIPE, stderr=PIPE)
                     = pipe.communicate()
                    if error:
                        print(error)
                        exit()

                    pipe.wait()
                    bcolors.print_text("OKGREEN", "repo {0} cloning in {1} ... DONE!".format(addon['repo'], addon['name_directory']))





def main(argv):
    _print_banner()
    if not argv:
        bcolors.print_text('ERROR', "Wrong Option")
        return False

    globals()[argv[0]](argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])
