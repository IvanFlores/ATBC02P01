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


# builds the Results class
class Results:

    # defines the constructor
    def __init__(self, pid, result):
        self.__pid = pid
        self.__result = result

    # returns the PID
    def get_pid(self):
        return self.__pid

    # returns the console results
    def get_result(self):
        return self.__result
