# Sistema de comunicación de texto (chat), de forma segura orientado a personas con discapacidad visual

Objetivos:
    • Aplicar los conceptos de cifrado
    • Aplicar los conceptos de encriptación
    • Reforzar la teoría de las transmisiones inalámbricas y se recomienda el envío de los paquetes a través de la red de Internet
    • Manejar adecuadamente el ruido en transmisiones, y corregir los posibles errores.
    
    Descripción del proyecto:
Se solicita la elaboración de un sistema de transmisión inalámbrica y bidireccional entre 2 computadoras.  Este sistema debe ser de carácter inclusivo, orientado a personas con problemas o discapacidad visual, que puedan escribir en teclado Braille.
Se deberá utilizar el método de transmisión de información utilizando la técnica de codificación y detección de errores para garantizar que el mensaje recibido, sea el mismo que el enviado, además de que, al estar cifrado y seguro, ya que únicamente la computadora que posea la manera de descifrarlo, podrá convertirlo al mensaje original.
Se deberán utilizar 3 tipos diferentes de cifrado: Hill, César y uno propio (desarrollado por cada grupo), y para elegir qué cifrado se usará, la computadora transmisora lo elegirá aleatoriamente, enviando como primera ráfaga al receptor, el tipo de cifrado utilizado.

Para chequear que el mensaje fue recibido se dejan unas de opciones:

    1. Como mínimo en el proyecto: presentar el mensaje en la pantalla del receptor.  Se hace la aclaración que esto no sería el proyecto completo para 2 personas con discapacidad visual, pero que podría funcionar para la interacción con personas sin discapacidad.  Para hacerlo completo debería de terminar el proyecto con cualquiera de los siguientes incisos.
    
    2. Traducir el mensaje recibido en voz, y enviarlo a una bocina, para que la persona lo pueda escuchar.  Si se realiza esta opción, se tendrá un bonus extra por realizarla equivalente a expolab.
    
    3. Enviar el mensaje recibido a una impresora e imprimirlo.  Asumiendo que para que esto sea utilizado por personas con discapacidad visual, sea una impresora Braille.  Si se realiza esta opción, se tendrá un bonus extra por realizarla será de 100 puntos en el proyecto o 10 puntos netos de la nota del curso.
    
La comunicación deberá realizarse mediante el lenguaje Python, y el protocolo que vincula ambas computadoras queda a discreción del estudiante, por ejemplo, hamachi.

Especificaciones:
    
    • Utilizará la codificación Hamming para la detección de posibles errores de transmisión, con la corrección de 1 bit por ráfaga es suficiente.
    
    • Deberá realizar el teclado alfabético con el sistema de escritura Braille, se recomienda exceptuar los caracteres numéricos, signos especiales y letras con acento; pero si algún grupo desea incluirlos, tiene libertad de hacerlo.
    
    • El receptor deberá contar con una bocina ya sea del ordenador o externa para reproducir el mensaje.  Es optativo
    
    • Utilizará el sistema de cifrado Hill, César y un extra, para la encriptación del mensaje.
    
    • La comunicación será estrictamente en el lenguaje Python, donde no se puede utilizar librerías para la encriptación y codificación del mensaje.
    
    • El mensaje deberá llevar ruido introducido por una secuencia aleatoria generada por la programación o por la comunicación que utilice el estudiante (en caso de que no desee usar Internet) con el fin de detectar errores.

Restricciones:
    
    • Se evaluará la versión bidireccional
    
    • Se pide la corrección de 1 bit de error, Hamming
    
    • Se verificará que la introducción del ruido sea de forma aleatoria

Proceso de Fases
    
    1. Primera: reporte IEEE formato LaTeX, propuestas, cronograma de actividades, materiales, bibliografía, etc.
   
    2. Segunda: reporte IEEE formato LaTeX, avances del proyecto, como mínimo 30%
    
    3. Tercera: proyecto terminado al 100% y reporte IEEE en formato LaTex, marco teórico, diseño, problemas en la realización, solución final, fotografías del proyecto paso a paso, fotografías de los integrantes realizando el proyecto, conclusiones, recomendaciones, bibliografía, etc.



Referencias bibliográficas:
    
    • https://www.gndiario.com/singchat-comunicarse-personas-discapacidad
    
    • https://www.xatakamovil.com/aplicaciones/siete-aplicaciones-para-personas-con-discapacidad-en-android-y-ios
    
    • https://youtu.be/ryRK9QllyD8 
