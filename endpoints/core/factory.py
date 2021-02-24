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

from endpoints.core.python_command import PythonCommand
from endpoints.core.java_command import JavaCommand



# runs a project
class Factory:

    # return the project result
    def run_project(self, parameters, language):

        if language == 'python':
            command = PythonCommand()
        elif language == 'java':
            command = JavaCommand()

        built_command = command.builder(parameters)
        result = command.executer(built_command)

        return result
