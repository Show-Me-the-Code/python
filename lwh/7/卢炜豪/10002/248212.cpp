#include<stdio.h>
#define n 65537
#include<math.h>
int prime[n],isprime[n];
int main()
{
    int cnt=1;
	prime[0]=1;
	prime[1]=0;
	for (int i=2; i*i<n;  i++)
	 {
	     if (prime[i]==0)
        {
		isprime[++cnt ]=i;
		for (int k=i*i; k<sqrt(n)&&k>=0; k+=i)
        prime[k]=1;

	  }
	 }
    int j=2,w,k=2,h;
    isprime[1]=1;
    int x,q=2;
      while(scanf("%d",&x)!=EOF)
      {
      int p=x;
      for(q=2;isprime[q]<x&&q<=56;q++)
      {
          while(x!=isprime[q])
          {
          if(x%isprime[q]==0)
          {
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
