#include<stdio.h>
#define n 100000
#include<math.h>
int prime[n],isprime[n];
int main()
{
    int cnt=1;
	prime[0]=1;
	prime[1]=0;
	//int n=66660;
	for (int i=2; i*i<n;  i++)
	 {
	  //   printf("i=%d\n",i);
	     if (prime[i]==0)
        {
		isprime[++cnt ]=i;
		//printf("isprime[%d]=%d\n",cnt,isprime[cnt]);
		for (int k=i*i; k<sqrt(n)&&k>=0; k+=i)
        {
			prime[k]=1;
		//	printf("k=%d\n",k);
        }
	  }

	 }
	// for(int i=0;i<n;i++) printf("%d\n",isprime[i]);
    int j=2,w,k=2,h;

    //以上代码求得素数表isprime
    isprime[1]=1;
  //  for(int hh=1;hh<sqrt(n);hh++)
 //   printf("!isprime[%d]=%d\n",hh,isprime[hh]);
    int x,q=2;
      while(scanf("%d",&x)!=EOF)
      {

    //  scanf("%d",&x);
      int p=x;
//      for(int i=1;i<)

      for(q=2;isprime[q]<x&&q<=56;q++)
      {
          while(x!=isprime[q])
          {
          if(x%isprime[q]==0)
          {
              //if(p==isprime[q]) printf("1");
              printf("%d ",isprime[q]);
              x=x/isprime[q];
             // printf("x=%d\n",x);
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
