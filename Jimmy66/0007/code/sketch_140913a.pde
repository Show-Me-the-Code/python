#测试
void setup()
{
size(800,800);
}
void draw()
{
background(0);
float r=random(0,mouseX);
println(r);
ellipse(400,400,r,r);
}
