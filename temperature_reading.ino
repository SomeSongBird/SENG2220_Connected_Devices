//setup variables first
int sensorPin = 0; //Thermometer pin
int LEDpin = 2; 
int LEDstate = 0;  
unsigned long time1 = 0; //needs to be the same type as what millis() returns

void setup()
{
  Serial.begin(9600);  //Start the serial connection with the computer
                       //to view the result open the serial monitor 
  digitalWrite(LEDpin,LEDstate);
  time1 = millis(); //get the initial time of the system
}
 
void loop()                     // this is the code that runs over and over again
{
  if(Serial.available()){ //check if there's something in the serial buffer
   byte whatIGot = Serial.read(); //read those bytes
   if(whatIGot == 'O'){LEDstate = 1000;} //if it is the same as an ascii O turn the LED on
   else if(whatIGot == 'I'){LEDstate = 0;} //if it is the same as an ascii I turn the LED off
   digitalWrite(LEDpin,LEDstate); //change the status of the LED
  }
  //Every 5 seconds read the temperature and send it over the Serial port
  if(millis()-time1>=5000){
    send_temp();
    time1 = millis(); 
  }
}

void send_temp(){
  int reading = analogRead(sensorPin);  
   
   // converting that reading to voltage, for 3.3v arduino use 3.3
   float voltage = reading * 5.0;
   voltage /= 1024.0; 
   
   // print out the voltage
   //Serial.print(voltage); Serial.println(" volts");
   
   // now print out the temperature
   float temperatureC = (voltage - 0.5) * 100 ;  //converting from 10 mv per degree wit 500 mV offset
                                                 //to degrees ((voltage - 500mV) times 100)
   //Serial.print(temperatureC); Serial.println(" degrees C");
   
   // now convert to Fahrenheit
   float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
   Serial.println(temperatureF); 
}
