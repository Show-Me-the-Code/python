#include <stdio.h>
int main()
{
    int n, a0,a1,a2,b0,b1,b2,c0,c1,c2,l0,l1,l2,w0,w1,w2;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d %d %d %d %d %d",&a0,&b0,&c0,&a1,&b1,&c1);

        c2=c0+c1;
        w2=c2%60;
        l2=c2/60;

        b2=b0+b1+l2;
        w1=b2%60;
        l1=b2/60;

        a2=a1+a0+l1;

        printf("%d %d %d\n",a2,w1,w2);
    }
}
