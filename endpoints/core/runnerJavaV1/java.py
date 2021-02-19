import subprocess


class Java:
    def __init__(self, java_path, java_file):
        self.java_path = java_path
        self.java_file = java_file
        self.java_file_path = ''
        self.java_file_name = ''
        # print('object java created \n\tjava path is: '+ self.java_path + "\n\tjava file is: " + self.java_file)

    def runner(self):
        string_runner = ''
        string_compiler = self.get_string_compiler()
        self.set_java_file_date()
        string_runner = self.get_string_runner()
        # se corre en consola
        command = string_compiler + " & " + string_runner
        subprocess.run(command, shell=True)

    def get_string_compiler(self):
        res = '"' + self.java_path + 'c" "' + self.java_file + '.java"'
        return res

    def set_java_file_date(self):
        # separate path file and name file
        lim = r"\q"
        i = len(self.java_file) - 1
        while i >= 0 and lim[0] != self.java_file[i] :
            i = i - 1
        self.java_file_name = self.java_file[i + 1:len(self.java_file)]
        self.java_file_path = self.java_file[0:i + 1]
        # print(self.java_file_path + '\t' + self.java_file_name)

    def get_string_runner(self):
        res = '"' + self.java_path + '" -cp ' + self.java_file_path + ' ' + self.java_file_name
        return res
