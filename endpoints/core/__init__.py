from endpoints.core.python_command import PythonCommand

# test if python command works (should be erased)
python_command = PythonCommand(r'D:\Juan\programas\python', r'C:\Users\Public', r'\command')
command = python_command.builder()
python_command.executer(command)
