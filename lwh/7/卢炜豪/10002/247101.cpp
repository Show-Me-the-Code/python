#include<stdio.h>
#include<string.h>
#define maxn 75545
int main()
{
    //先用筛法求出素数表，放进数组prime中
    //1表示是素数，0表示表示不是素数

    int prime[maxn],isprime[maxn],i,j;//先假设全部都是素数
    int n=266;
    for(int i=0;i<n;i++)
        prime[i]=1;
    for(int i=2;i<n;i++)
    {
         //printf("～");
       if(prime[i]==1)
       {
           for(int j=i;j<n;j++)
           {
               prime[j*i]=0;
              // printf("i*j=%d\n",i*j);
              //printf("!");

           }
       }
    }
    j=1;
    for(int i=1;i<n;i++)
    {

        if(prime[i]==1)
        {

            isprime[j]=i;
            j++;

        }
    }
    //for(i=1;i<j;i++) printf("%d\n",isprime[i]);

    //以上代码求得素数表isprime
   // printf("!%d\n",isprime[5]);
      int x,q=2;
      while(scanf("%d",&x)!=EOF)
      {

    //  scanf("%d",&x);
      int p=x;
//      for(int i=1;i<)

      for(q=2;isprime[q]<x;q++)
      {
          while(x!=isprime[q])
          {
          if(x%isprime[q]==0)
          {
              //if(p==isprime[q]) printf("1");
              printf("%d ",isprime[q]);
              x=x/isprime[q];
          }
          else
          break;
          }



      }
      if(x==p)
      printf("1 %d\n",x);
      else printf("%d\n",x);
      }




}
