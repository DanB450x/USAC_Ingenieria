'''
#################################################################
# Programa para encriptación de mensaje cesar                   #
#                                                               #
# Nombre de integrantes:                                        #
#   Héctor Fernando Carrera Soto                                #
#   Oscar                                                       #
#   Nestor                                                      #
#                                                               #
# Ingeniería electrónica - 2S 2021                              #
# Laboratorio comunicaciónes 2                                  #
#################################################################
'''


import threading
'''permite que una aplicación ejecute simultáneamente varias operaciones en
el mismo espacio de proceso se llama Threading.'''

import socket
'''Los sockets se pueden comunicar dentro de un proceso, entre procesos dentro
de la misma máquina o entre procesos de máquinas de continentes diferentes.'''

print("")
host = input('Digite la ip del servidor: ') #host_number #Este será nuestro host local
puerto = int(input('Digite el puerto al cual desea unirse como host: ')) #En toería este debería ser un puerto sólido y estable

print("")
nickname = input("Seleccióne su nickname: ")
print("")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, puerto))

def recibiendo():
    while True:
        try: #Todo el tiempo estaremos recibiendo del servidor
            mensaje = client.recv(1024).decode('utf-8') #Seguimos recibiendo del servidor
            #1024 es el numero de bytes, no olvidar

            if mensaje == 'NICK':
                client.send(nickname.encode('utf-8'))
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
        print("")
        mensaje = f'{format(nickname)}: {input("")} \n' #Siempre estaremos esperando un mensaje
        client.send(mensaje.encode("utf-8"))

recibiendo_thread = threading.Thread(target=recibiendo) #Ejecutamos los subprocesos de ricepción y uno de verificación
recibiendo_thread.start() #Iniciamos el procesos

write_thread = threading.Thread(target=write)
write_thread.start() #Iniciamos la función de escritura
