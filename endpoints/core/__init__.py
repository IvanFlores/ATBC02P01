'''
# example how to run factory

from endpoints.core.factory import Factory
from endpoints.core.python_parameters import PythonParameters

factory = Factory()
result = factory.run_project(r'D:\Juan\programas\python', r'C:\Users\Public', 'command', 'python')
print(result.get_result())

'''