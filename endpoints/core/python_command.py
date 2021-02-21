#
# @video_converter.py Copyright (c) 2020Jalasoft
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

# this class ads the python executable path and the python project path


class PythonCommand:

    def __init__(self, executable_path, project_path):
        self.executable_path = executable_path
        self.project_path = project_path

    # this function run the python command
    def run_python_project(self):
        p = subprocess.Popen(self.build_command(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line.decode('ascii')),
        p.wait()

    # this function builds the command tu run the python project main class
    def build_command(self):
        return r'{}\main.py'.format(self.executable_path+' '+self.project_path)
