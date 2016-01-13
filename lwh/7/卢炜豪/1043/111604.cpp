#include<stdio.h>
#include<math.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        double rate;
        rate=pow(0.95,n);

        printf("%.2lf\n",rate*100);
    }
}
