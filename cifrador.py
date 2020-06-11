#diccionario de letras y numeros orden alfabetico y una que otra letra de otros alfabetos
global letras
letras = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'P','k':'Y','l':'U','m':'I',
'n':'R','o':'Q','p':'W','q':'S','r':'G','s':'K','t':'L','u':'N','v':'X','w':'C','x':'V','y':'B','z':'J','.':'0',
' ':'@','_':'-','A':'Д','B':'Б','C':'Ж','D':'З','E':'И','F':'Л','G':'Ф','H':'Ц','I':'Ч','J':'Ш','K':'Щ','L':'Ъ',
'M':'Ы','N':'Ь','O':'Ю','P':'Ѳ','Q':'Ѣ','R':'Ѱ','S':'Ѡ','T':'Ѫ','U':'Ѭ','V':'ß','W':'å','X':'ö','Y':'あ','Z':'お'}

#diccionario contrario al primero
global letras_cifradas
letras_cifradas = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','P':'j','Y':'k','U':'l',
'I':'m','R':'n','Q':'o','W':'p','S':'q','G':'r','K':'s','L':'t','N':'u','X':'v','C':'w','V':'x','B':'y','J':'z',
'0':'.','@':chr(32), '-':chr(95),'Д':'A','Б':'B','Ж':'C','З':'D','И':'E','Л':'F','Ф':'G','Ц':'H','Ч':'I','Ш':'J',
'Щ':'K','Ъ':'L','Ы':'M','Ь':'N','Ю':'O','Ѳ':'P','Ѣ':'Q','Ѱ':'R','Ѡ':'S','Ѫ':'T','Ѭ':'U','ß':'V','å':'W','ö':'X',
'あ':'Y','お':'Z'}

#arreglo de contraseñas generadas con anterioridad, el sistema de contraseña para archivos esta algo defectuoso
global passwords_gen
passwords_gen = ['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']

#funcion para cifrar archivos, pienso que debe de haber una forma un poco mas corta
def cifrar():
	#importamos librerias para recorrer directorios, de tiempo , de sistema, random, getpass para el nombre de usuario
	#y math para calculos ligeros
	from os import walk
	from time import time
	import os, math, random, getpass
	user = getpass.getuser() #obtenemos el nombre de usuario del computador
	#ruta , esto se describe solo
	ruta = input("Ruta que usted quiera encriptar, separa por (\\->si es windows) y (//->si es linux): ")#"D:\\lab\\files"
	#contadores
	cont = 0
	contador_archivo = 0
	#inicializamos la variable tiempo
	inicio = time()
	#lo mismo de los anteriores codigos, supongo que ya saben esto de memoria ajja
	for root, dirs, files in walk(ruta):
		for archivos in files:
			(nombreArchivo, extension) = os.path.splitext(archivos)
			#obtenemos el nombre del archivo
			largo = len(nombreArchivo)
			contador_archivo += 1
			#------------------- codigo de pruebas , eso era en el comienzo -----------
			#print("Archivos encontrados: " + str(nombreArchivo + extension), end="\n")
			#"".join(random.choice(letras) for x in range(largo))
			#nueva_lista = [print(x) for x in [1,2,3,4,5,6] if x < 5]
			#nueva_lista = [x for x in [1,2,3,4,5,6] if x < 5]
			#--------------------------------------------------------------------------
			#c pasa a ser igual al contador
			c = cont + 1
			#luego c crea un arreglo por archivo encontrado, pienso que consume un poquillo pero 
			#me funciona bien , y no hay problema
			c = []
			#para l en archivos
			for l in archivos:
				#recorro las llaves y valores del diccionario
				for k,v in letras.items():
					#si la llave esta en el l que recorre a archivos
					if k in l:
						#se agrega el valor de la letra en el arreglo c
						c.append(v)
			#a es igual a los arreglos que contiene c
			a = "".join(c)
			#se modifica el nombre del archivo junto con su extension por el cifrado obtenido
			mod = os.rename(root + "\\" + nombreArchivo + extension, root + "\\" + a)
			#se muestra el antes y despues del archivo cifrado.
			print(a, mod)
	print("""
		ARCHIVOS CIFRADOS POR UN HASH ---- QUE TENGA UN BUEN DIA

				""")
	#final es el tiempo de ejecucion
	final = time() - inicio
	#se muestra el tiempo + cantidad de archivos + el tiempo
	print("Tiempo que tomo en cifrar "+ str(contador_archivo) +" archivos: " + str(round(final, 2)) + "Segundos")
	#se genera de manera aleatoria una contraseña para luego poder usarla
	gen_ = random.choice(passwords_gen)
	#se crea un archivo con la contraseña generada
	archivo_password = open('password_generada_'+user+'.txt','w')
	archivo_password.write(gen_)
	archivo_password.close()
	#se muestra la contraseña generada y que se a creado el archivo con esta misma.
	print("Contraseña generada para decifrar sus archivos: " + str(gen_) + " y archivo creado ")

def decifrar():
	#en este codigo es lo mismo del anterior solo que se modifican algunas lineas
	from time import time
	from os import walk
	import os, math
	ruta = input("Ruta para poder decifrar sus archivos: ")
	contador = 0
	contador_archivo = 0
	inicio = time()
	#esta no se que hace, pero funciona tal cual esta asi.
	gen_rand = random.choice(passwords_gen)
	verificar = input("Ingrese contraseña generada: ")
	for root, dirs, files in walk(ruta):
		for archivos in files:
			(nombreArchivo, extension) = os.path.splitext(archivos)
			contador_archivo += 1
			c_d = contador + 1
			c_d = []
			#para pg en la contraseña generada
			for pg in passwords_gen:
				#si pg esta en verificar
				if pg in verificar:
					#se imprime la contraseña que se ingreso
					print(":u" + str(pg) + "u:")
					#para cada letra sobre el nombre del archivo
					for letra in nombreArchivo:
						#para las llaves decifrar, valores decifrar en los items de las letras cifradas
						for k_d, v_d in letras_cifradas.items():
							#si la llave esta en la letra
							if k_d in letra:
								#me agrega el valor a los arreglos de c_d
								c_d.append(v_d)
					#lo mismo que en cifrar
					b = "".join(c_d)
					moder = os.rename(root + "\\" + archivos, root + "\\" + b)
					print(b, moder)
					print("""		
						SUS ARCHIVOS VOLVIERON A LA NORMALIDAD
						""")
					final = time() - inicio
					print("Tiempo que tomo en cifrar "+ str(contador_archivo) +" archivos: " + str(round(final, 2)) + " Segundos")

import random, string

def gen_pass():
	archivo = open("ruta+core.core_","wb")
	gen_l = 64
	contador = 0
	for y in range(0, 120):
		gen_letras = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase
		gen_c = "".join(random.choice(gen_letras) for x in range(gen_l))
		#contenido_arreglo = contador + 1
		#contenido_arreglo = []
		#contenido_arreglo.append(gen_c)
		archivo.write("'".encode())
		archivo.write(gen_c.encode())
		archivo.write("'".encode())
		archivo.write(",".encode())
	print("Creado")

def menu():
	import time, getpass, platform, os, sys
	user = getpass.getuser()
	os = platform.system()
	procesador = platform.machine()
	fecha = time.strftime("%d/%m/%y")
	#dia = time.strftime("%a")
	hora = time.strftime("%H : %M : %S")
	print("""
		
		PRIVIET, MY LITTLE SCRIPT
		****************************************************************
		SI ESTAS USANDO ESTE SCRIPT DIVIERTETE!!!
		****************************************************************

		""")
	print("""
		*****************************************
		***   ****************************    ***
		***     1) C                          ***
		***     2) D                          ***
		***     0)Salir		              ***
		***                                   ***
		***   ****************************    ***
		***         ***************           ***
		***    *************************      ***
		*****************************************
		***           Usuario: """+ user + 
		"""          *** \n"""
		"""    		***        Fecha actual: """ + fecha +
		"""     *** \n"""
		"""    		***       Hora actual: """ + hora +
		"""   *** \n"""
		"""    		***      Sistema operativo: """ + os +
		"""   ***\n"""
		"""    		***          Procesador: """ + procesador +
		"""          ***\n    		*****************************************
		"""
		"""
		"""
	"""
	"""
	)
	opcion = input("#~ ")
	if opcion == '1':
		cifrar()
	elif opcion == '2':
		decifrar()
	elif opcion == '0':
		sys.exit(0)

if '__name__':
	menu()
