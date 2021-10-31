#include <Keyboard.h>


int led1=0;
int led1s=0;
int led2=0;
int led2s=0;
int led3=0;
int led3s=0;
int led4=0;
int led4s=0;
int led5=0;
int led5s=0;
int led6=0;
int led6s=0;
int led7=0;
int led7s=0;
int actnum=0;
int actnums=0;

void setup() {
  Keyboard.begin();
  Serial.begin(9600);
  
    delay(1000);
  pinMode(0, INPUT);
  pinMode(1, OUTPUT);
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, INPUT);
  pinMode(7, OUTPUT);
  pinMode(8, INPUT);
  pinMode(9, OUTPUT);
  pinMode(10, INPUT);
  pinMode(11, OUTPUT);
  pinMode(12, INPUT);
  pinMode(13, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, OUTPUT);
  }


void loop() {
  delay(500);
  led1= digitalRead(0);
  led2= digitalRead(2);
  led3= digitalRead(4);
  led4= digitalRead(6);
  led5= digitalRead(8);
  led6= digitalRead(10);
  led7= digitalRead(12);
  actnum=digitalRead(A0);

  if(led1==HIGH){led1s=1-led1s;
  if(led1s==1){digitalWrite(1, HIGH);}
                else{digitalWrite(1,LOW);}}


  if(led2==HIGH){led2s=1-led2s;
  if(led2s==1){digitalWrite(3, HIGH);}
                else{digitalWrite(3,LOW);}}

  if(led3==HIGH){led3s=1-led3s;
  if(led3s==1){digitalWrite(5, HIGH);}
                else{digitalWrite(5,LOW);}}

  if(led4==HIGH){led4s=1-led4s;
  if(led4s==1){digitalWrite(7, HIGH);}
                else{digitalWrite(7,LOW);}}

  if(led5==HIGH){led5s=1-led5s;
  if(led5s==1){digitalWrite(9, HIGH);}
                else{digitalWrite(9,LOW);}}

  if(led6==HIGH){led6s=1-led6s;
  if(led6s==1){digitalWrite(11, HIGH);}
                else{digitalWrite(11,LOW);}}

  if(actnum==HIGH){actnums=1-actnums;
  if(actnums==1){digitalWrite(A1, HIGH);}
                else{digitalWrite(A1,LOW);}}


  if(led7==HIGH){led7s=1-led7s;}


  if(led1s==0 && led2s==1&& led3s==0 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print("A");
    led7s=0;
    delay(500);}
  //else
   if(led1s==0 && led2s==1 && led3s==0 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("B");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==1 && led3s==0 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("C");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==1 && led3s==1 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("D");
    led7s=0;
    delay(500);}
  //else
   if(led1s==0 && led2s==1 && led3s==1 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("E");
    led7s=0;
    delay(500);}
   if(led1s==1 && led2s==1 && led3s==0 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("F");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==1 && led3s==1 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("G");
    led7s=0;
    delay(500);}
  //else
   if(led1s==0 && led2s==1 && led3s==1 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("H");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==0 && led3s==0 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("I");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==0 && led3s==1 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("J");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==1 && led3s==0 && led4s==0 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("K");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==1 && led3s==0 && led4s==1 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("L");
    led7s=0;
    delay(500);}


   if(led1s==1 && led2s==1 && led3s==0 && led4s==0 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("M");
    led7s=0;
    delay(500);}

 
   if(led1s==1 && led2s==1 && led3s==1 && led4s==0 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("N");
    led7s=0;
    delay(500);}


   if(led1s==0 && led2s==1 && led3s==1 && led4s==0 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("O");
    led7s=0;
    delay(500);}

   if(led1s==1 && led2s==1 && led3s==0 && led4s==1 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("P");
    led7s=0;
    delay(500);}

   if(led1s==1 && led2s==1 && led3s==1 && led4s==1 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("Q");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==1 && led3s==1 && led4s==1 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("R");
    led7s=0;
    delay(500);}

   if(led1s==1 && led2s==0 && led3s==0 && led4s==1 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("S");
    led7s=0;
    delay(500);}


   if(led1s==1 && led2s==0 && led3s==1 && led4s==1 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("T");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==1 && led3s==0 && led4s==0 && led5s==1 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("U");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==1 && led3s==0 && led4s==1 && led5s==1 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("V");
    led7s=0;
    delay(500);}

   if(led1s==1 && led2s==0 && led3s==1 && led4s==1 && led5s==1 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print ("W");
    led7s=0;
    delay(500);}

   if(led1s==1 && led2s==1 && led3s==0 && led4s==0 && led5s==1 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("X");
    led7s=0;
    delay(500);}

   if(led1s==1 && led2s==1 && led3s==1 && led4s==0 && led5s==1 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("Y");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==1 && led3s==1 && led4s==0 && led5s==1 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("Z");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==0 && led3s==0 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print (" ");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==0 && led3s==1 && led4s==1 && led5s==1 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print (".");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==0 && led3s==0 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==0){
    Keyboard.print (",");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==0 && led3s==0 && led4s==1 && led5s==1 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("?");
    led7s=0;
    delay(500);}

   if(led1s==0 && led2s==0 && led3s==1 && led4s==1 && led5s==0 && led6s==1 && led7s==1 && actnums==0){
    Keyboard.print ("!");
    led7s=0;
    delay(500);}



  if(led1s==1 && led2s==0&& led3s==1 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print("0");
    led7s=0;
    delay(500);}
  if(led1s==0 && led2s==1&& led3s==0 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print("1");
    led7s=0;
    delay(500);}
  //else
   if(led1s==0 && led2s==1 && led3s==0 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("2");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==1 && led3s==0 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("3");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==1 && led3s==1 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("4");
    led7s=0;
    delay(500);}
  //else
   if(led1s==0 && led2s==1 && led3s==1 && led4s==0 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("5");
    led7s=0;
    delay(500);}
   if(led1s==1 && led2s==1 && led3s==0 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("6");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==1 && led3s==1 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("7");
    led7s=0;
    delay(500);}
  //else
   if(led1s==0 && led2s==1 && led3s==1 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("8");
    led7s=0;
    delay(500);}
  //else
   if(led1s==1 && led2s==0 && led3s==0 && led4s==1 && led5s==0 && led6s==0 && led7s==1 && actnums==1){
    Keyboard.print ("9");
    led7s=0;
    delay(500);}




  
    
  }
  
  






                
