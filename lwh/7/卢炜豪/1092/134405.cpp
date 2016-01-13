#include<stdio.h>
#include<stdlib.h>
  int main()
  {
      int a,b,n;
      while(scanf("%d%d",&a,&b)&&(a!=0&&b!=0))
      {
          n=1;
          while(b>0)
          {
             n=(n*a)%1000;
             b--;
          }
             printf("%d\n",n);
     }
     return 0;
 }
