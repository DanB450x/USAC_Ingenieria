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

#host_number = input(str("Ingrese puerto del host: "))
print("")
host = input('Digite la ip de su servidor: ') #host_number #Este será nuestro host local
puerto = int(input('Digite el puerto al cual desea unirse como host: ')) #En toería este debería ser un puerto sólido y estable

#Crear un conector INET, STREAMing
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Vinculamos el servidor al host y la dirección IP
servidor.bind((host, puerto))
servidor.listen() #Hacemos que nuestro servidor

clientes = [] #Creando una lista de clientes
nicknames = [] #Creando lista de nicknames
'''
Esto servirá para obtener el nombre y apodo de cada nuevo cliente.
'''

#Definiendo función de transmisión a todos los clientes conectados
def broadcast(mensaje):
    #El broadcast es la difusión masiva de información o paquetes de datos a través de redes informáticas.
    for client in clientes:
    #por cada cliente que ahora esté conectado, vamos a decir que el cliente me envió un mensaje
        client.send(mensaje) #Al recibir un mensaje, se lo enviaremos a todos los clientes

#A continuación, cundo un cliente envíe un mensaje, lo prosesaremos y reenviaremos a todos incluido al mismo cliente
def handle(client):
    while True: #Creamos un bucle para el chat
        try:
            mensaje = client.recv(1024) #Especificamos los bytes recibidos por el cliente
            broadcast(mensaje) #Diremos que solo transmitiremos el mensaje

        except: #Esto es para que no encontremos errores al cerrar el chat por parte del cliente
            index = clientes.index(client)
            clientes.remove(client)
            client.close()
            nickname = nicknames[index] #Los nicknames estará en el indica
            broadcast(f'{nickname} a abandonado el chat.'.format(nickname).encode('utf-8')) #Avisamos que el cliente se ha ido del chat
            '''
            El apodo del clienteson los del indice, así que básicamente el apodo será el nombre,
            el cual será almacenado en el indice.
            '''
            nicknames.remove(nickname)
            break #si no hacemos esto, el programa tirará error al ver que un cliente ya no se encuentra
'''
Para cada cliente tendremos un solo hilo
'''
#------------------------------------Definiendo métodos principales de recepción----------------------------------------
#Uniremos todo en una sola función

def recibiendo():
    while True: #Básicamente aceptamos todas la conexiónes
        client, address = servidor.accept() #Obtenemos el cliente y la dirección del mismo
        print(f"Conectado con {format(str(address))}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clientes.append(client)

        print(f'Tu nickname de cliente es {format(nickname)}! \n')
        print("")
        broadcast(f'{format(nickname)} ha ingresado al chat! \n'.encode('utf-8')) #Avisamos a todos que el cliente ha ingresado
        client.send('Conectado al servidor!'.encode('utf-8'))
        print("")

        thread = threading.Thread(target=handle, args=(client,)) #Esto permite llevar varios procesos a la vez
        thread.start() #Iniciando varios procesos

print("")
print('Información de la conexión:')
print("IP del servidor: ",host)
print("Puerto del servidor: ",puerto)
print("")
print("----El servidor está escuchando----")
print("")

recibiendo()

'''
Notas: La función DECODE realiza comparaciones de igualdad entre argumentos, tratando también los valores nulos
como iguales, para determinar qué argumento se devolverá como resultado.
'''
