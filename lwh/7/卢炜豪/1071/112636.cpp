#include<stdio.h>
#include<math.h>
int main()
{
    int a,b;
    while(scanf("%d %d",&a,&b)!=EOF)
    {
        int add0=0,add1=0;
        add0=pow(a,b);
        add1=pow(b,a);
        if(add0>add1) printf("%d\n",a);
        else printf("%d\n",b);
    }
}
