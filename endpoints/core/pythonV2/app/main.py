from java import Java

if __name__ == '__main__':
    # primer argumento java path
    java_path = r'C:\Program Files\Java\jdk1.8.0\bin\java'
    # segundo argumento main file path
    java_file = r'C:\Users\Trabajo\Desktop\saludo\src\saludo\Saludo'
    # tercer argumento array de paquetes
    java_packages = [r'paquete']
    # creacion del objeto java con los path recibidos
    java = Java(java_path, java_file, java_packages)
    # llamada a la funcion runner de Java
    java.runner()
