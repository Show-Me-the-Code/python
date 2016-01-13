#include<stdio.h>
int main()
{
    int x;;int a,b,c;a=b=c=1;
    while(scanf("%d",&x)!=EOF)
    {
        int i=0;
        for(a=1;a<=100;a++)
        {
            for(b=1;b<=50;b++)
            {
                for(c=1;c<=20;c++)
                {
                    if(x==(a+2*b+5*c))
                    i=i+1;

                }
            }
        }
       printf("%d\n",i);
    }
return 0;

}
