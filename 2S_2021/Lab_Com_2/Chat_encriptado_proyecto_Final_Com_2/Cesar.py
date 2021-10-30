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

#---------------------------------Paquetes--------------------------------------
from sympy.crypto.crypto import encipher_shift,decipher_shift
'''
El paquete encipher_shift y decipher_shift hacer llamado al cifrado cesar, el cifrado cesar
también se le conoce también como cifrado de desplazamiento
'''
import random
#random contiene una serie de funciones relacionadas con los valores aleatorios


#
def Cesar_selec():
    print("Encriptado cesar: enable")
#

def Programa_cesar():

    print("")
    #------------------------Aquí va el código-----------------------------------------
    #>>>>>>>Menú
    print('                     ======================================================')
    print('                    ||   Bienvenido al programa de cifrado y decifrado    ||                        ')
    print('                    ||             Comunicaciónes 2 - 2021                ||                        ')
    print('                    ||              Versión final - Cesar                 ||                        ')
    print('                     ======================================================')
    print('')
    print('===========================================================================================================')
    print('Menú:')
    print('')
    print('1. Cifrado')
    print('2. Decifrado')
    print('')
    opcion = int(input('Ingrese una opción: '))
    print('===========================================================================================================')
    print('')



    if opcion == 1:
    #>>>>>>>Generando pin de cifrado
        cif1 = int(input("Escoja el nivel de encriptación: \n"))
        cif2 = cif1*(-1)
        print("")
        #Pedimos al usuario que escoja un nivel de encriptado para generar un código único de decifrado
        key1 = random.randint(cif2, cif1)
        print("Código de cifrado: \n", key1)
        #Key escoje el nivel de encriptación

        #>>>>>>Encriptado
        print("")
        mensaje = input(str("Inserte un mensaje para encriptación cesar: \n"))
        mensaje = mensaje.upper().replace(" ", "");
        #Pedimos un dato '\n' da un salto de línea
        cifrado = encipher_shift(mensaje, key1)
        print("")
        #Encriptamos el mensaje, var = mensaje, espacio de desplazamient del cifrado= 1
        print("mensaje encriptado: \n",cifrado)

    elif opcion == 2:
        #>>>>>>Desencriptación
        print("")
        key2 = input(f"Ingrese el código único de descifrado: \n")
        #Pide el código único de decifrado
        key3 = int(f" {key2}")
        #Deja un espacio en blanco, para que no se tenga que estar dejando
        #key4 = key3*(-1)
        print("")
        mensaje_cif1 = input(str('Ingrese el mensaje encriptado: \n'))
        #Pide el mensaje encriptado
        mensaje_cif2 = str(f" {mensaje_cif1}")
        #Deja un espacio en blanco, para que no se tenga que estar dejando
        print("")
        decifrar = decipher_shift(mensaje_cif2, key3)
        print("mensaje decifrado: \n", decifrar)

    else:
        print("Opción no encontrada.")

def main():
    Cesar_selec()

main()
