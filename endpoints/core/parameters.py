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

# ads the binary path, the project path and the name of the project
class Parameters:

    # builds the Parameters class
    def __init__(self, path_binary, path_projects, name_project):
        self.__path_binary = path_binary
        self.__path_projects = path_projects
        self.__name_project = name_project

    # return the binary path
    def get_path_binary(self):
        return self.__path_binary

    # return the project path
    def get_path_projects(self):
        return self.__path_projects

    # return the project name
    def get_name_project(self):
        return self.__name_project
