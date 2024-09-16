const int pinLed = 8;
int status=0;
void setup() {
  // put your setup code here, to run once:
  //Reloj Monumental Santa Catarina Villanueva
  //Puerto serial
  Serial.begin(9600);
  //Configurar puerto 13
  pinMode(pinLed,OUTPUT);
  digitalWrite(pinLed, HIGH);
}

void loop() {
  if(Serial.available()>0)
  {
    char dt =Serial.read();
    if(dt >='1' && dt <='3' && status==0)
    {
      digitalWrite(pinLed, LOW);
      //delay(1000);
      status=1;
    }
    if(dt >= '4' && dt <=7 && status==1)
    {
      digitalWrite(pinLed, HIGH);
      //delay(1000);
      status=0;
    }
  }
  /*
  // put your main code here, to run repeatedly:
  digitalWrite(pinLed,HIGH);
  //Envia informacion al puerto serial PC
  Serial.println("I am a Arduino Board");
  delay(1000);
  digitalWrite(pinLed,LOW);
  delay(1000);
  */
}
