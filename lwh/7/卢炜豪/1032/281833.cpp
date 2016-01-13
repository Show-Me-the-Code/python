#include <stdio.h>
int main()
{
int x,y;
while(scanf("%d %d",&x,&y)!=EOF)
  {
int a=x,b=y;
int i;double area=0;
for(;;)
{
scanf("%d %d",&x,&y);
area=area+(b+y)*(x-a)/2.0;
a=x;b=y;
if(y==0) break;
}
printf("%.1lf\n",area);
}
}
