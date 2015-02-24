int []x={200,400};
int i;
void round(int a, int b){
 ellipse(a,b,100,100); 
}
void setup(){          
  size(600,600);
  smooth();
  ellipseMode(RADIUS);
  
}
void draw(){
  background(255);
  /*
  if(mousePressed==true) 
  {  
    fill(0); 
  }  
  */
  for(i=0;i<2;i++)
  {
    if(dist(mouseX,mouseY,x[i],x[i])<100) fill(255,128,0);
  else fill(255);
   round(x[i],x[i]);
  
  }
 
}
