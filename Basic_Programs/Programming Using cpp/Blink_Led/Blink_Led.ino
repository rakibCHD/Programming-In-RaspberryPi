/*
-->Board Manager Url:https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
-->Board: "Raspberry Pi Pico"
-->Flash Size: "2MB (no FS)"
-->CPU Speed: "125 MHz"
-->Debug Port: "Disabled"
-->Debug Level: "None"
-->Port: First time no need, After Upload a Sketch ,Connect the port.
-->On Board Built-in Green Led connected with pin 25.
*/

int led = 25;

void setup() 
{
  pinMode(led, OUTPUT);       
}

void loop()
{              
  digitalWrite(led, HIGH);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000);
                             
} 
