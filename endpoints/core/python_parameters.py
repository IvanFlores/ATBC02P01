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


from endpoints.core.parameters import Parameters

# this class ads the parameters for python command


class PythonParameters(Parameters):

    # this function ads the python parameters to parameters super class
    def __init__(self, path_binary, path_projects, name_project):
        super().__init__(path_binary, path_projects, name_project)
