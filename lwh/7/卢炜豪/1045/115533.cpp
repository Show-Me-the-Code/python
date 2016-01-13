#include<stdio.h>
int main()
{
    int day[2][13]={
    {0,31,28,31,30,31,30,31,31,30,31,30,31},
    {0,31,29,31,30,31,30,31,31,30,31,30,31}
    };

    int year,month;char useless;
    while(scanf("%d%c%d",&year,&useless,&month)!=EOF)
    {
        int m,n;
        if((year%4==0&&year%100!=0)||(year%400==0))
            m=1;
        else m=0;
        //printf("%d %d\n",m,n);

        if(m==1)
        {
            n=1;
            printf("%d\n",day[n][month]);
        }
        else if(m==0)
        {
            n=0;
            printf("%d\n",day[n][month]);
        }


    }
    return 0;
}
