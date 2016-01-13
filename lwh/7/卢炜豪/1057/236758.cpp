#include<stdio.h>
#include<math.h>
#include<stdlib.h>
double JC(int n);
int main()
{
    double x;int n;
    while(scanf("%lf %d",&x,&n)==2)
    {
        int q=1;
        int m=1;
        double fz=1,l=0;long long int fm;
        while(1)
        {
            fm=JC(m);
            fz=pow(x,m);
          //  printf("fz=%.5lf fm=%lld ",fz,fm);
            l=l+q*(fz/fm);
        //    printf("l=%.5lf ",l);
            q=-q;
            m=m+2;
            double p=pow(10,-n);
            double b=abs(fz/fm);
        //    printf("fz/fm=%.5lf\n",fz/fm);
            if(b<p)
            break;
        }
        printf("%.*lf\n",n,l);
    }
}
double JC(int n)
{
   long long  int result=1;
    for(int i=n;i>0;i--)
    {
        result=result*i;
    }
   // printf("result=%d\n",result);
    return result;
}
