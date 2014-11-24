#include <Servo.h> 
Servo FBLikeservo; 
int FBLikeAngle = 45;  
int FBLikeStartAngle = 110; 


void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT); 
  Serial.println("Start");  
  FBLikeservo.attach(9); 
  FBLikeservo.write(FBLikeStartAngle);
}
 
void loop() {
  // get any incoming bytes:
  if (Serial.available() > 0) {
    int thisChar = Serial.read();
    
    Serial.write(thisChar);
    //Serial.println(thisChar);
    
    if (thisChar == 'B')
    {
     
       FBLikeservo.write(FBLikeAngle);   
       delay(2000);                     
       FBLikeservo.write(FBLikeStartAngle);      // waits for the servo to get there 
       delay(200);
       
       /*
       //Once get the notice when likecount is changed and to trigger Servo to action. 
       //Use LED 13 to debug first 
       digitalWrite(13, HIGH);   // sets the LED on
       delay (200); 
       digitalWrite(13, LOW);   // sets the LED on
       delay (200);
       */
     }
    }
  }

