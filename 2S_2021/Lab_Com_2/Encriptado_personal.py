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

#
def Personal_selec():
    print("Encriptado personalizado: enable")
#

def Programa_personal():

        print("")
        print('                     ======================================================')
        print('                    ||   Bienvenido al programa de cifrado y decifrado    ||                        ')
        print('                    ||             Comunicaciónes 2 - 2021                ||                        ')
        print('                    ||           Versión final - Personalizado            ||                        ')
        print('                     ======================================================')
        print('')

    TAM_MAX_CLAVE = 26

    def obtenerModo():
     while True:
       print('¿Deseas encriptar o desencriptar un mensaje?')
       modo = input().lower()
       if modo in 'encriptar e desencriptar d'.split():
        return modo
       else:
        print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')


    def obtenerMensaje():
      print('Ingresa tu mensaje:')
      return input()

    def obtenerClave():
      clave = 0
      while True:
        print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
          return clave

    def obtenerMensajeTraducido(modo, mensaje, clave):
        if modo[0] == 'd':
         clave= -clave
        traduccion = ''
        for simbolo in mensaje:
             if simbolo.isalpha():
                 num = ord(simbolo)
                 num += clave

                 if simbolo.isupper():
                     if num > ord('Z'):
                         num -= 26
                     elif num < ord('A'):
                         num += 26
                 elif simbolo.islower():
                     if num > ord('z'):
                            num -= 26
                     elif num < ord('a'):
                         num += 26

                 traduccion += chr(num)
             else:
                 traduccion += simbolo
        return traduccion

    modo = obtenerModo()
    mensaje = obtenerMensaje()
    clave = obtenerClave()

    print('Tu texto traducido es:')
    print(obtenerMensajeTraducido(modo, mensaje, clave))


def main():
    Personal_selec()

main()
