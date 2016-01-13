#include<stdio.h>
#define maxn 200005
int main()
{
    int m,key,a[maxn];
    scanf("%d %d",&m,&key);
    for(int i=0;i<m;i++)
    {
        scanf("%d",&a[i]);
    }
    for(int i=0;i<m;i++)
    {
        if(key==a[i])
        {
            printf("%d\n",i);
            break;
        }
        else
        {
            printf("NO\n");
            break;
        }
    }
}
