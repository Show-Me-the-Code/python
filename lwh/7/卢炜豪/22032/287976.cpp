#include<stdio.h>
int main()
{
    int c;
    while(scanf("%d",&c)==1&&c!=0)
    {
       int a[100000];
       for(int i=0;i<c;i++)
        scanf("%d",&a[i]);

        printf("%d\n",a[c-1]-a[0]+1-c);
    }
}
