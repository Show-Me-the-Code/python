#include <cstdio>
#define add(x) (x)*(x)
int main()
{
    int N,l1,l2;
    double a[500+2],b[500+2];
    scanf("%d",&N);
    for(int i=0;i<N;i++)
        scanf("%lf %lf",&a[i],&b[i]);
    double max=0;
    for(int i=0;i<N-1;i++)
        for(int j=i+1;j<N;j++)
        {
            if(add(a[i]-a[j])+add(b[i]-b[j])>max)
            {
                max=add(a[i]-a[j])+add(b[i]-b[j]);
                l1=i;l2=j;
            }
        }
        printf("%d %d\n",l1+1,l2+1);
}
