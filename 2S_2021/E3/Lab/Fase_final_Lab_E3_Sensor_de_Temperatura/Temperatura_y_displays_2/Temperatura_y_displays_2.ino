/**************************************************
*   Laboratorio de electrónica 3 - 2S_2021        *
*   Sensor de temperatura arduino + fpga          *
*   Integrantes:                                  *
*     Nicole Alejandra López Calderón , 201800683 *
*     Daniel Estuardo Blanco Girón, 201632135     *
*     Héctor Fernando Carrera Soto, 201700923     *
***************************************************/


/*********************
* Llamando dibrerías *
*********************/


#include <Adafruit_MLX90614.h>
#include "SevSeg.h"
// Documentación de la librería: https://github.com/DeanIsMe/SevSeg/blob/master/README.md

/**********************
* Creando instancias  *
**********************/

SevSeg sevseg; // Crear una instancia de un objeto controlador de siete segmentos
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

/********************
* Definiendo pines  *
********************/

int led_rojo = 10;
int led_verde = 11;
int buzz = 12;
float temperatura;

/************************************
* Creando configuraciónes de pines  *
************************************/

void setup() {

  pinMode(led_rojo, OUTPUT);
  pinMode(led_verde, OUTPUT);
  pinMode(buzz, OUTPUT);

  /*************************************
  * Configurando sensor de temperatura *
  *************************************/

  Serial.begin(9600);
  while (!Serial);

  Serial.println("Adafruit MLX90614 test");

  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  };

  Serial.print("Emissivity = "); Serial.println(mlx.readEmissivity());
  Serial.println("================================================");

  /************************
  * Configurando displays *
  *************************/

  byte numDigits = 3; // Número de displays
  byte digitPins[] = {A3, A2, A1}; // En donde van conectados los comm
  byte segmentPins[] = {2, 3, 4, 5, 6, 7, 8, 9}; // Pindes de la A ...F y el punto
  bool resistorsOnSegments = false; // 'false' quiere decir que las resistencias están en los pines comm
  byte hardwareConfig = COMMON_ANODE; // See README.md for options
  bool updateWithDelays = false; // Default 'false' is Recommended
  bool leadingZeros = false; // Usar 'true' si quiero que se muestren los ceros
  bool disableDecPoint = false; // Use 'true' if your decimal point doesn't exist or isn't connected

  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments,
  updateWithDelays, leadingZeros, disableDecPoint);

  // El brillo se puede ajustar usando un valor entre -200 y 200. 0 a 100 es el rango estándar.
  sevseg.setBrightness(90);
}

/******************
* Iniciando loop  *
*******************/

void loop() {
  temperatura = mlx.readObjectTempC();

  if(temperatura > 38){
    accion(1,0,1);
  }
  else if (temperatura < 36) {
    accion(1,0,1);
  }
  else{
    accion(0,1,0);
  }

  Serial.print(temperatura); Serial.println("*C");
  sevseg.setNumber(temperatura*10, 1);
  delay(10);
  sevseg.refreshDisplay(); // Must run repeatedly


}

/************
* Acciones  *
************/

void accion( int estado_rojo,  int estado_verde,  int estado_buzz){
  digitalWrite(led_rojo, estado_rojo);
  digitalWrite(led_verde, estado_verde);
  digitalWrite(buzz, estado_buzz);
}

/// END ///
