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

from endpoints.core.command import Command

# this class ads  builds the python command


class PythonCommand(Command):

    # this function builds the command to run the python project main class
    def builder(self, python_parameters):
        return r'{}\main.py'.format(python_parameters.get_path_binary() + ' ' + python_parameters.get_path_projects() +
                                    python_parameters.get_name_project())
