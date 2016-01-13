#include <stdio.h>
int main()
{

  int x,y;
  while(scanf("%d %d",&x,&y)!=EOF)
  {

        int x,y;
        int a=0,b=0;
        int i;double area=0;
        for(;;)
        {

        scanf("%d %d",&x,&y);
        area=area+(b+y)*(x-a)/2;
        a=x;b=y;
        if(x!=0&&y==0) break;
        }

        printf("%.1lf\n",area);


}
}
