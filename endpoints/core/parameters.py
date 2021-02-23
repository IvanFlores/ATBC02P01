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


# this class ads the binary path, the project path and the name of the project


class Parameters:

    def __init__(self, path_binary, path_projects, name_project):
        self.__path_binary = path_binary
        self.__path_projects = path_projects
        self.__name_project = name_project

    def get_path_binary(self):
        return self.__path_binary

    def get_path_projects(self):
        return self.__path_projects

    def get_name_project(self):
        return self.__name_project
