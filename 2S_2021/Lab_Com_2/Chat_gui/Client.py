#-------------------------------------------------------------------------------
'''
Proyecto comunicaciónes 2 - 2S_2021

Integrantes:
    Héctor Fernando Carrera Soto, 201700923
    Oscar Jose Urizar Orozco, 201504352
    Nestor Eduardo de León Aguilón,201906466
'''
#-------------------------------------------------------------------------------

import threading
'''permite que una aplicación ejecute simultáneamente varias operaciones en
el mismo espacio de proceso se llama Threading.'''

import socket
'''Los sockets se pueden comunicar dentro de un proceso, entre procesos dentro
de la misma máquina o entre procesos de máquinas de continentes diferentes.'''

nickname = input("Seleccióne su nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

def recibiendo():
    while True:
        try: #Todo el tiempo estaremos recibiendo del servidor
            mensaje = client.recv(1024).decode('ascii') #Seguimos recibiendo del servidor
            #1024 es el numero de bytes, no olvidar

            if mensaje == 'NICK':
                client.send(nickname.encode('ascii'))
                #pass #la línea anterior y esta es solo para obtener el Nick
            else:
                print(mensaje) #Para ver lo que el host tiene que decirnos

        except: #Para cuando cierre conexión
            print("Un error ha ocurrido!")
            client.close()
            break #Cerramos ciclo


#------------------------Definiendo función de escritura------------------------

def write(): #Siempre definiremos un nuevo mensaje
    while True:
        mensaje = f'{nickname}: {input("")}' #Siempre estaremos esperando un mensaje
        client.send(mensaje.encode("ascii"))

recibiendo_thread = threading.Thread(target=recibiendo) #Ejecutamos los subprocesos de ricepción y uno de verificación
recibiendo_thread.start() #Iniciamos el procesos

write_thread = threading.Thread(target=write)
write.start() #Iniciamos la función de escritura
