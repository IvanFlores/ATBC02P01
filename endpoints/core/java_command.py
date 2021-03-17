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


from endpoints.core.command import Command


# builds the JavaCommand class
class JavaCommand(Command):

    # Returns a array with the necessary commands tu run project
    def builder(self, java_parameters):
        list = []
        list.append(self.get_compiler_command(java_parameters))
        list.append(self.get_runner_command(java_parameters))
        return list

    # builds the command run file
    def get_runner_command(self, java_parameters):
        return 'cd ' + java_parameters.get_path_projects() + ' & "' + java_parameters.get_path_binary() + '" ' + java_parameters.get_name_project() + '.main'

    # builds the command compile
    def get_compiler_command(self, java_parameters):
        return '"' + java_parameters.get_path_binary() + 'c" ' + java_parameters.get_path_projects() + '\\' + java_parameters.get_name_project() + '\\*.java'
