from scipy.io.wavfile import read
import matplotlib.pyplot as plt
#import pyaudio
import numpy as np
from PIL import Image
from scipy.signal import hilbert


print('')
#print(' ____  _                           _     _               _                                                         _                          _       _           _               _____ _____ _________      __')
#print('|  _ \(_)                         (_)   | |             | |                                                       | |                        | |     | |         | |             / ____/ ____|__   __\ \    / /')
#pritn('| |_) |_  ___ _ ____   _____ _ __  _  __| | ___     __ _| |  _ __  _ __ ___   __ _ _ __ __ _ _ __ ___   __ _    __| | ___ _ __ ___   ___   __| |_   _| | __ _  __| | ___  _ __  | (___| (___    | |   \ \  / /')
#print('|  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \   / _` | | | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \ / _` |  / _` |/ _ \ '_ ` _ \ / _ \ / _` | | | | |/ _` |/ _` |/ _ \| '__|  \___ \\___ \   | |    \ \/ /  ')
#print('| |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | (_| | | | |_) | | | (_) | (_| | | | (_| | | | | | | (_| | | (_| |  __/ | | | | | (_) | (_| | |_| | | (_| | (_| | (_) | |     ____) |___) |  | |     \  /')
#print('|____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_| | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_|\__,_|  \__,_|\___|_| |_| |_|\___/ \__,_|\__,_|_|\__,_|\__,_|\___/|_|    |_____/_____/   |_|      \/    ')
#print('                                                            | |               __/ |                                                                                                                            ')
#print('                                                            |_|              |___/                                                                                                                             ')

print('                     ================================================')
print('                    ||   Bienvenido al programa demodulador SSTV    ||                        ')
print('                    ||          Comunicaci??nes 1 - 2021             ||                        ')
print('                    ||                 Versi??n 1                    ||                        ')
print('                     ================================================')
print('')
print('===========================================================================================================')
print('Recuerde que cada archivo a analizar debe de estar en la carpeta de este programa y ser extensi??n (.wav) .')
print('')
name_file = input('Ingrese el nombre del archivo sin la extensi??n: ')
print('===========================================================================================================')
print('')

#-- Inicializamos variable srate
SRate = 44100

#-- Creando array (image)
img = Image.new( 'L', (140,140), "white")
pixelData = img.load()

#-- copiando todas las muestras en una matriz
input_data = read(f"{name_file}.wav")
audio = input_data[1]

#-- Generando el vector transformado de Hilbert de las muestras
analytic_signal = hilbert(audio)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
i_frequency = np.diff(instantaneous_phase) / (2.0*np.pi) * SRate


#-- Trazar el gr??fico de frecuencia a lo largo del tiempo
plt.plot(i_frequency)
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [s]')
plt.show()

lineCount = 0
sampleBuffer = 0
#-- Busque los pulsos de sincronizaci??n de l??nea (debe estar aproximadamente por encima de 190 muestras por debajo de 1300 hz)
for i in range(0, len(i_frequency)-2800):

    #-- Si la frecuencia est?? por debajo de 1300Hz, comience a contar
    if(i_frequency[i] < 1300):
        sampleBuffer = sampleBuffer + 1

    #-- Si se encuentran m??s de 207 muestras por debajo de la frecuencia dada, incremente el recuento de l??neas
    if(sampleBuffer > 207):
        lineCount = lineCount + 1
        sampleBuffer = 0

        lineBuffer = 0
        lineIndex = 0
        #-- Agarre los datos de la l??nea completa
        for j in range(i, i + 2700):
            lineBuffer = lineBuffer + 1
            if(lineBuffer > 22):
                lineBuffer = 0

                #-- Map each individual data point into a pixel value
                if(i_frequency[j] < 1500):
                    pixelData[lineIndex,lineCount] = 0
                elif(i_frequency[j] > 2300):
                    pixelData[lineIndex,lineCount] = 255

                #-- Asigne cada punto de datos individual en un valor de p??xel
                else:
                    pixelData[lineIndex,lineCount] = np.int(((i_frequency[j] - 1500.0)/800.0)*255.0)

                #-- Salta una l??nea
                lineIndex = lineIndex + 1


    #-- Comprobaci??n de seguridad para evitar la detecci??n de l??neas adicionales
    if(i_frequency[i] > 1300):
        sampleBuffer = 0

print("-- Recuento de l??neas --")
print(lineCount)
print("-- Sample Rate / Frecuencia de muestreo --")
print(SRate)
print("-- Number of Samples / N??mero de muestras--")
print(len(i_frequency))
print("")
print("== Operaci??n completa, precione cualquier tecla para continuar... ==")
#raw_input()

#-- Mostrar la imagen resultante
img.show()
