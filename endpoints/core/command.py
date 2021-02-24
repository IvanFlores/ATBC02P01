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
from abc import abstractmethod
from endpoints.core.results import Results


# builds the Command class
class Command:

    # defines the constructor for its children
    @abstractmethod
    def builder(self, parameters):
        pass

    # runs an array of commands and shows the last result
    def executer(self, commands):
        for command in commands:
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            p.wait()
        pid = p.pid
        res = ''
        for line in p.stdout.readlines():
            res = res + line.decode('ascii')
        return Results(pid, res)
