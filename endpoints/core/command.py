#
# @ide_jala.py Copyright (c) 2021 Jalasoft
# 2643Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# Av. General Inofuentes esquina Calle 20,Edificio Union № 1376, La Paz, Bolivia
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft
#

import subprocess

# this class ads the binary path, the project path and the name of the project


class Command:

    def __init__(self, path_binary, path_projects, name_project):
        self.path_binary = path_binary
        self.path_projects = path_projects
        self.name_project = name_project

    # this function is set to build commands on subclasses
    def builder(self):
        pass

    # this function can run any command
    def executer(self, command):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line.decode('ascii')),
        p.wait()
