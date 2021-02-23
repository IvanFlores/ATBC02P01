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

from java_command import JavaCommand
from java_parameters import JavaParameters

if __name__ == '__main__':
    # primer argumento java path
    java_path = r'C:\Program Files\Java\jdk1.8.0\bin\java'
    # segundo argumento project path
    java_project_path = r'E:\tests\saludo2\src'
    # tercer argumento nombre del proyecto
    java_project_name = 'saludo'
    # creacion del objeto java_paremeters con los datos recibidos
    java_parameters = JavaParameters(java_path, java_project_path, java_project_name)
    # creacion del objeto java con el objeto java_parameters
    java = JavaCommand()
    # llamada a la funcion compiler de Java
    compiler = java.compiler(java_parameters)
    print('command compiler: ' + compiler)
    res = java.executer(compiler)
    print('\tPID: ' + str(res.get_pid()) + '\n\tRespuesta: ' + res.get_result())
    # llamada a la funcion builder de Java
    builder = java.builder(java_parameters)
    print('command builder: ' + builder)
    res = java.executer(builder)
    print('\tPID: ' + str(res.get_pid()) + '\n\tRespuesta: ' + res.get_result())
