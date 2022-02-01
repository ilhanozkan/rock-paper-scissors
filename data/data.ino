int p1_1 = 8;
int p1_2 = 9;
int p2_1 = 12;
int p2_2 = 13;

void setup() {
  Serial.begin(9600);
  
  pinMode(p1_1, INPUT);
  pinMode(p1_2, INPUT);
  pinMode(p2_1, INPUT);
  pinMode(p2_2, INPUT);
}

void loop() {
  int value1_1 = digitalRead(p1_1);
  int value1_2 = digitalRead(p1_2);
  int value2_1 = digitalRead(p2_1);
  int value2_2 = digitalRead(p2_2);

  Serial.println(String(value1_1) + String(value1_2) + ";" + String(value2_1) + String(value2_2));
  delay(300);
}
