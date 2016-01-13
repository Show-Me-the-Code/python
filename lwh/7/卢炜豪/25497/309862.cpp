#include <cstdio>
int main()
{
    int n;
    while(scanf("%d",&n)==1&&n!=-1)
    {
        double k=n;
        double sum=0;
        while(k>=1)
        {
            sum=sum+n/k;
            k--;
        }
        printf("%.1lf\n",sum);
    }
}
