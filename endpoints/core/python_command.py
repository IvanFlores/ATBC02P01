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


# builds the PythonCommand class
class PythonCommand(Command):

    # Returns a array with the necessary commands tu run project
    def builder(self, python_parameters):
        return [r'{}\main.py'.format(python_parameters.get_path_binary() + ' ' + python_parameters.get_path_projects() +
                                    '\\' + python_parameters.get_name_project())]
