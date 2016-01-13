#include<stdio.h>
double cal(double n);
int main()
{
    double n;char s[11];
    int x;double k;
    scanf("%d",&x);
    for(int i=1;i<=x;i++)
    {
        scanf("%s %lf",s,&n);
        k=cal(n);
        printf("%s %.2lf\n",s,k);
    }
}
double cal(double n)
{
    double sum;
    if(n<=10&&n>=0)
    {
        sum=n*4.0/3.0;
    }
    else if(n>10&&n<=20)
    {
        sum=n*2.5-10.5;
    }
    else if(n>20)
    {
        sum=n*3.4-5;
    }
    return sum;
}
