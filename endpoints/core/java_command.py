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
from endpoints.core.command import Command

# this class ads  builds the python command


class JavaCommand(Command):

    def __init__(self, path_binary, path_projects, name_project):
        super().__init__(path_binary, path_projects, name_project)

    # this function builds the command to run the python project main class
    def builder(self):
        return 'cd ' + self.path_projects + ' & "' + self.path_binary + '" ' + self.name_project + '.main'

    def compiler(self):
        return 'cd ' + self.path_projects + ' & "' + self.path_binary + 'c" ' + self.name_project + '\\*.java'
