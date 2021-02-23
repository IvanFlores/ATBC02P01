#
# @ide_jala.py Copyright (c) 2021 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
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
from endpoints.core.command import Command

# this class ads  builds the java command


class JavaCommand(Command):

    # this function builds the command to run the java project main class
    def builder(self, java_parameters):
        #return 'cd ' + java_parameters.get_path_projects() + ' & "' + java_parameters.get_path_binary() + '" ' + java_parameters.get_name_project() + '.main'
        return f'cd {java_parameters.get_path_projects()} & "{java_parameters.get_path_binary()}" {java_parameters.get_name_project()}.main'

    # this function builds the command to compile the java project
    def compiler(self, java_parameters):
        return '"' + java_parameters.get_path_binary() + 'c" ' + java_parameters.get_path_projects() + '\\' + java_parameters.get_name_project() + '\\*.java'
