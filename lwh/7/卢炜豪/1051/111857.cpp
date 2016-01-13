#include<stdio.h>
#include<math.h>
int rec(int x,int n);
int main()
{
    int x,n;
    while(scanf("%d %d",&x,&n)!=EOF)
    {

        printf("%d\n",rec(x,n));
    }
}
int rec(int x,int n)
{
    int sum=0;
       if(n==0)
        return sum;

       else
        sum=pow(-1,n+1)*pow(x,n)+rec(x,n-1);

        return sum;
}
