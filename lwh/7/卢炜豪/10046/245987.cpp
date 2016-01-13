#include<stdio.h>
#include<math.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int q=2;
        for(int i=1;i<n;i++)
            q=q*2%2012;
        int p=2*n%2012;;
        int laste=(p+q-1)%2012;
        printf("%d\n",laste);
    }
}
