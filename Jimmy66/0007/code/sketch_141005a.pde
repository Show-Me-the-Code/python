int i=0;
void setup(){          
  size(600,800);        
  smooth();          
  ellipseMode(RADIUS);    
}
void draw(){
  i++;
  background(255);
  if(i==1) fill(255,0,0);
  else fill(0);
  ellipse(300,150,80,80);
  if(i==2)  fill(255,255,0);
  else fill(0);
  ellipse(300,350,80,80); 
  if(i==3) fill(0,255,0);
  else fill(0);
  ellipse(300,550,80,80); 
  i=i%3;
  delay(1000);
}
