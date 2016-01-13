#include<stdio.h>
int main()
{
    int n,x,num;
    while(1)
    {
        int t=0;
        scanf("%d %d",&n,&x);
        int a[n];
        if(n==0&&x==0) break;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&num);
            a[i]=num;
        }
        for(int i=0;i<n;i++)
        {

         //printf("%d\n",a[i]);
         if(x==a[i])
         {


            t=i+1;

          printf("%d\n",t);
          break;
         }


         else if(a[i]!=x)
            t++;
         if(t==n) printf("-1\n");
        }

     //  printf("%d\n",t);



    }
}
