import subprocess

from setuptools import command


class Java:
    def __init__(self, java_path, java_file, java_packages):
        self.java_path = java_path
        self.java_file = java_file
        self.java_packages = java_packages
        self.java_package_path = ''
        self.java_file_name = ''
        self.java_package_name = ''
        self.command_cd = ''
        # print('object java created \n\tjava path is: '+ self.java_path + "\n\tjava file is: " + self.java_file)

    def runner(self):
        self.set_java_file_data()
        self.compiler()
        self.run_file()

    def compiler(self):
        i = 0
        lim = r"\q"
        while i < len(self.java_packages):
            package = self.java_packages[i]
            command_compiler = self.command_cd + ' & "' + self.java_path + 'c" ' + self.java_package_name + lim[0] + package + lim[0] + '*.java'
            i = i + 1
            self.execute(command_compiler)
        i = i + 1
        command_compiler = self.command_cd + ' & "' + self.java_path + 'c" ' + self.java_package_name + lim[0] + '*.java'
        self.execute(command_compiler)

    def set_java_file_data(self):
        # separate path file and name file
        lim = r"\q"
        i = len(self.java_file) - 1
        flag = 2
        flag_pos = 0
        while i >= 0 and flag > 0:
            if lim[0] == self.java_file[i] and flag == 2:
                self.java_file_name = self.java_file[i + 1:len(self.java_file)]
                flag_pos = i
                flag = flag - 1
            else:
                if lim[0] == self.java_file[i] and flag == 1:
                    self.java_package_name = self.java_file[i + 1:flag_pos]
                    flag_pos = i
                    flag = flag - 1
            i = i - 1
        self.java_package_path = self.java_file[0:flag_pos]
        self.command_cd = 'cd ' + self.java_package_path
        # print(self.java_package_path + '\t' + self.java_package_name + '\t' + self.java_file_name)

    def run_file(self):
        command_runner = self.command_cd + ' & "' + self.java_path + '" ' + self.java_package_name + '.' + self.java_file_name
        self.execute(command_runner)

    def execute(self, com):
        p = subprocess.Popen(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line.decode('ascii')),
        p.wait()
