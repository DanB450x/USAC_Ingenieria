#----------------------------------------------------------------------------------------------------------------------------------------
                                                                    #Nestor
#----------------------------------------------------------------------------------------------------------------------------------------
'''
NumPy es un paquete de Python que significa “Numerical Python”, es la librería principal para la informática científica,
proporciona potentes estructuras de datos, implementando matrices y matrices multidimensionales. Estas estructuras de datos garantizan
cálculos eficientes con matrices.
'''
import numpy as np;
'''
Este módulo proporciona acceso a las funciones matemáticas definidas en el estándar de C.
'''
import math

#Definimos una función imprimir_matriz
def imprimir_matriz(charar):
    #Definimos el tamaño de filas, el cual se encuentra en el rango de 1 a 2
    for i in range(2):
        #Definimos el tamaño de columnas, el cual se encuentra en el rango de 1 a 2
        for j in range(2):
            #Dividimos en 2 columnas y 1 fila la cadena de caractéres ingresados.
            print(int(charar[i][j]), "\t", end='')
        #imprimimos un salto de línea una vez realizada la operación
        print("\n");


print("")
#------------------------Aquí va el código-----------------------------------------
#>>>>>>>Menú
print('                     ======================================================')
print('                    ||   Bienvenido al programa de cifrado y decifrado    ||                        ')
print('                    ||             Comunicaciónes 2 - 2021                ||                        ')
print('                    ||                 Versión 5 - Hill                   ||                        ')
print('                     ======================================================')
print('')
print('===========================================================================================================')
print('Menú:')
print('')
print('1. Cifrado')
#print('2. Decifrado')
print('')
print('===========================================================================================================')
opcion =int(input("Opción: "))
print('===========================================================================================================')
print('')


#Colocamos una condicional if para seleccionar las opciónes que vemos en el menú
if opcion == 1:
    #Solicitar Datos
    Texto = input("Por favor introduzca el texto a cifrar: ");
    #upper = pasa todo a mayúsculas | replace = Elimina espacio entre caractéres.
    Texto = Texto.upper().replace(" ", "");
    print("Por favor introduzca la clave (matriz 2x2)");
    #Devuelve una nueva matriz de forma y tipo dados, sin inicializar entradas.
    Clave = np.empty((4, 4));
    msj="";
    #Devuelve una nueva matriz de forma y tipo dados, llena de ceros.
    m_crip=np.zeros((math.ceil(len(Texto)/2),2))

    for i in range(2):
        for j in range(2):
            # el símvolo + concatena una variable, con el resto del mensaje a imprimir
            msj="Posición "+str(i)+","+str(j)+": ";
            #Vamos pidiendo la matriz
            Clave[i][j] = input(msj);

    imprimir_matriz(Clave)
    #Comenzamos a crear nuestro diccionario
    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    #----------------------------------------------------------------------------------------------------------------------------------------
                                                                    #Fernando
    #----------------------------------------------------------------------------------------------------------------------------------------

    cipher="";
    #Inicializando variables
    i=0
    j=0
    #En el caso de while True la expresión siempre va a ser evaluada como verdadera por definición. Volviendo a nuestra traducción equivaldría a:
    #mientras verdadero sea verdadero: hacer algo
    while True:
        '''
        El bloque try se usa para verificar algún código en busca de errores, es decir, el código dentro del bloque
        try se ejecutará cuando no haya ningún error en el programa.
        Mientras que el código dentro del bloque except se ejecutará siempre que el programa encuentre algún error
        en el bloque try anterior.
        '''
        try:
            #Devuelve el número de elementos a lo largo de un eje dado.
            if (np.size(m_crip) / 2 == j):
                #Detenemos el ciclo
                break
            #i+1 es un contador que se suma de uno en uno
            print(Texto[i], " - ", Texto[i+1])
            m_crip[j][0]=diccionario_letras[Texto[i]]
            m_crip[j][1]=diccionario_letras[Texto[i+1]]
            #i aumenta de dos en dos
            i+=2
            #j aumenta de uno en uno
            j+=1

        except:
            #En esta parte, comenzamos a imprimir en una columna, el mensaje original y en otra su equivalente encriptado
            print(Texto[i])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            break

        #----------------------------------------------------------------------------------------------------------------------------------------
                                                                    #Oscar
        #----------------------------------------------------------------------------------------------------------------------------------------

    #for i in range(m_crip.length)

    c1 = 0
    c2 = 0
    m1 = 0
    m2 = 0
    #Devuelve una nueva matriz de forma y tipo dados, llena de ceros.
    cipher=np.zeros(m_crip.shape)
    print("Texto Cifrado")
    for i in range(int(np.size(m_crip)/2)):

        m1 = m_crip[i][0]
        m2 = m_crip[i][1]
        c1 = Clave[0][0]*m1 + Clave[1][0]*m2
        c2 = Clave[0][1] * m1 + Clave[1][1] * m2
        cipher[i][0]=c1%26
        cipher[i][1] = c2%26

        #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
        print(abecedario[int(cipher[i][0])],"",abecedario[int(cipher[i][1])]," ", end='')
        #print('')



else:
    print("                                                 ^     ")
    print("                                                / \    ")
    print("                                               / ! \    ")
    print("                                              /_____\   ")
    print("                                       Programa en progreso :3")


    '''
    #Descifrar
    # Solicitar Datos
    Texto = input("Por favor introduzca el texto a descifrar: ");
    Texto = Texto.upper().strip().replace(" ", "");
    print("Por favor introduzca la clave (matriz 2x2)");
    Clave = np.empty((4, 4));
    msj = "";
    m_crip = np.zeros((math.ceil(len(Texto) / 2), 2))

    for i in range(2):
        for j in range(2):
            msj="Posición"+str(i)+","+str(j)+": ";
            Clave[i][j] = input(msj);

    imprimir_matriz(Clave)
    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    #Inversa de una matriz A^-1=1/[A] * (A*)^T
    #Sacar determinante
    Determinante=Clave[0][0]*Clave[1][1]-Clave[0][1]*Clave[1][0]
    Adjunta=np.zeros((2,2))
    Adjunta[0][0] = Clave[1][1]
    Adjunta[1][1] = Clave[0][0]
    Adjunta[0][1] = -1*Clave[1][0]
    Adjunta[1][0] = -1*Clave[0][1]

    TAdj = np.zeros((2,2))
    TAdj[0][0] = Adjunta[0][0]
    TAdj[1][1] = Adjunta[1][1]
    TAdj[0][1] = Adjunta[1][0]
    TAdj[1][0] = Adjunta[0][1]

    Determinante=Determinante%26
    InClave = np.zeros((2, 2))
    InClave[0][0]= ((1/Determinante)*TAdj[0][0])%26
    InClave[0][1]= ((1 / Determinante) * TAdj[0][1])%26
    InClave[1][0]= ((1 / Determinante) * TAdj[1][0])%26
    InClave[1][1]= ((1 / Determinante) * TAdj[1][1])%26

    """
    print("Determinante ",Determinante)
    print("Adjunta ")
    for i in range(2):
        for j in range(2):
            print(Adjunta[i][j], "\t", end='')
        print("\n");
    print("Adjunta Transpuesta")
    for i in range(2)
        for j in range(2)
            print(TAdj[i][j], "\t", end='')
        print("\n");

    print("Matriz Inversa de la clave ")
    for i in range(2):
        for j in range(2):
            print(InClave[i][j], "\t", end='')
        print("\n");
    """

    i = 0
    j = 0
    while True:
        try:
            if (np.size(m_crip) / 2 == j):
                break
            #print(Texto[i], " - ", Texto[i + 1])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            m_crip[j][1] = diccionario_letras[Texto[i + 1]]
            i +=2
            j +=1

        except:
            print(Texto[i])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            break
    # for i in range(m_crip.length)

    c1 = 0
    c2 = 0
    m1 = 0
    m2 = 0
    #Devuelve el número de elementos a lo largo de un eje dado.
    descipher = np.zeros(m_crip.shape)
    print("Texto Descifrado: ")
    for i in range(int(np.size(m_crip) / 2)):
        m1 = m_crip[i][0]
        m2 = m_crip[i][1]
        c1 = InClave[0][0] * m1 + InClave[1][0] * m2
        c2 = InClave[0][1] * m1 + InClave[1][1] * m2
        descipher[i][0] = c1 % 26
        descipher[i][1] = c2 % 26

        #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
        print(abecedario[int(descipher[i][0])], "", abecedario[int(descipher[i][1])], " ", end='')
        #print('')
    '''
