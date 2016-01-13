#include<stdio.h>
#define maxn 1005
int main()
{
    int N,L;
    while(scanf("%d %d",&N,&L)==2&&(N!=0&&L!=0))
    {
        int a[maxn];char direct[maxn];
        for(int i=0;i<N;i++)
            scanf("%d %c",&a[i],&direct[i]);


        int max=0;
        for(int i=0;i<N;i++)
        {
            if(direct[i]=='L')
                a[i]=a[i];
            else if(direct[i]=='R')
                a[i]=L-a[i];

            if(a[i]>max)
                max=a[i];
        }
        printf("%d\n",max);
    }
}
