#include <stdio.h>

int a[10000+2];

int main()

{

   int t,l,r,n,q,ans;

   scanf("%d",&t);

   while(t)

   {

       scanf("%d",&n);

       for(int i=0;i<=n+1;i++)

           a[i]=0;

       scanf("%d",&q);

       for(int i=0;i<q;i++)

       {

           scanf("%d%d",&l,&r);

           for(int j=l;j<=r;j++) a[j]++;

       }

       for(int i=1;i<=n;i++)

       {

           printf("%d\n",a[i]);

       }
       t--;

   }

   return 0;

}
