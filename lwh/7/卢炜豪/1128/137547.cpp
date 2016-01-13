#include<stdio.h>
#define maxn 9999
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        double i0=1,i1=1,fz,result=0;
        double q0=0,q1=1,fm;
        int d=n;
        for(;d>0;d--)
        {
            fz=i0+i1;
            i1=i0;
            i0=fz;

            fm=q0+q1;
            q0=q1;
            q1=fm;
            result=result+fz/fm;
        }
        printf("%.10lf\n",result);
    }
}
