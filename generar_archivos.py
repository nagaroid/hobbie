# -*- coding: utf-8 -*-
print("""
 BIENVENIDO A MI GENERADOR DE ARCHIVOS CON NOMBRE ALEATORIO Y PESO ALEATORIO
 AQUI DE POR SI IBA A COLOCAR UN BANNER CON MI PSEUDONIMO PERO ME DIO FLOJERA
 ESPERO TE SIRVA TANTO COMO A MI.
 """)
from os import walk #libreria walk para recorrer directorios
import string, random, os, math # string para usar caracteres ascii para las cadenas, random para generar algun dato aleatorio
cont = 0#contador    # os libreria del sistema y math para calcular
largo = 8# largo del nombre
contenido = 10 # contenido del archivo
tamano_total = 0 # tamaño total creado
#obtener_tamaño = 0
letras = string.ascii_lowercase + string.ascii_uppercase #para el nombre del archivo
extensiones = ['.doc','.txt','.pdf','.docx','.xlsx','.rar','.jpg','.png','.cdr'] #las extensiones disponibles
#el tamaño en bytes(creo)
tamano = [1000000,2000000,3000000,4000000,50000000,60000000,7000000,8000000,9000000,10000000,11000000,12000000,13000000,14000000,15000000,16000000,17000000,18000000,190000000,20000000,21000000,22000000,23000000,24000000,25000000]
#entrada por teclado para generar archivos , pueden ir de 1 a el numero que quieran, claro que depende
#de la velocidad del pc y de almacenamiento
archivos_generar = int(input("Cantidad deseada de archivos a generar: "))
#ruta donde se guardaran los archivos
ruta_creacion = "D:\\ejercicios_python\\archivos_prueba\\" #str(input("Ruta donde desea crear los archivos para pruebas: "))
#pequeña advertencia, del peso de los archivos
print("El peso de cada archivo varia entre 1MB hasta 25MB")
#cantidad en un rango de 0 hasta el numero ingresado
for cantidad in range(0, archivos_generar):
    #cantidad pasa a ser una letra aleatoria por el rango del largo del nombre
     cantidad = "".join(random.choice(letras) for x in range(largo))
     print(largo)
     #content es el nombre del archivo
     content = "".join(random.choice(letras) for x in range(contenido))
     #extensiones random
     extension = random.choice(extensiones)
     #tamaño del archivo generado
     cantidad_tamano = random.choice(tamano)
     #contador de archivos
     cont += 1
     #archivo abre la ruta de la creacion + nombre del archivo + el numero del archivo + la extension
     archivo = open(ruta_creacion+cantidad+"-"+str(cont)+ extension,'wb')
     #dentro se escribe algun contenido aleatorio (solo por hacer peso)
     archivo.write(content.encode())
     #se escribe un salto de linea
     archivo.write("\n".encode())
     #se le da el tamaño al archivo escogido en megas
     archivo.seek(cantidad_tamano - 1)
     #se escribe un byte(no recuerdo bien que hace esto ejej)
     archivo.write(b"\0")
     #se cierra el archivo escrito
     archivo.close()
     #al final se muestra la cantidad de archivos generados + contador + nombre del archivo y la extension
     print("Cantidad de archivos generados: " + str(cont) + " | Nombre del archivo: " + str(cantidad) + " | Extension: " + str(extension))