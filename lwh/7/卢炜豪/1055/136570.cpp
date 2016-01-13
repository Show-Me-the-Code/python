#include<stdio.h>
#define maxn 10005
#define maxn1 65
int main()
{
     int n,b[maxn],i,min,max;
     char a[maxn][maxn1];
     while(scanf("%d",&n)!=EOF)
     {
          if(n==0)break;
          getchar();
          scanf("%s",&a[0][0]);
          scanf("%d",&b[0]);
          getchar();
          min=max=0;
          for(i=1;i<n;i++)
          {
               scanf("%s",&a[i][0]);
               scanf("%d",&b[i]);
               if(b[max]<b[i])max=i;
               if(b[i]<b[min])min=i;
               getchar();
          }
          printf("%s %s\n",&a[max][0],&a[min][0]);
     }
     return 0;
}
