#include<stdio.h>
#define maxn 200005
int main()
{
    int m,key,a[maxn],b[maxn];
    scanf("%d",&m);
    scanf("%d",&key);
    for(int i=0;i<m;i++)
    {
        scanf("%d",&a[i]);
    }
    int k=0;int d,w=0;
    for(int i=0;i<m;i++)
    {
      if(a[i]==key)
      {
      b[w]=i;
      k++;
      w++;
      }
}
    if(k==0) printf("NO\n");
    else
    {
        for(int i=0;i<w;i++)
        {
            if(i!=w-1)
            printf("%d ",b[i]);
            else printf("%d\n",b[i]);
        }
    }
}
