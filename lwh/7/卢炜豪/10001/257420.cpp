/*先用筛法求出6-10000之间的所有素数，存进一个数组中，
输入一个测试的数据，用for进行枚举，得到离这个数据最接近又小于他的一个素数，。。不说了先写代码看看会不会超时先
*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#define maxn 100000000
int prime[maxn],isprime[maxn];
int main()
{
    int x;
    scanf("%d",&x);
    int cnt=2;
    long long int edge=x*x;
    memset(prime,0,sizeof(prime));
    memset(isprime,0,sizeof(isprime));
  //  printf("%d",prime[199]);
    prime[0]=0;
    prime[1]=0;
    prime[2]=0;
    for(int i=2;i*i<edge;i++)
    {
       // printf("i=%d\n",i);
        if(prime[i]==0)
        {
            isprime[cnt]=i;
            printf("isprime[%d]=%d\n",cnt,isprime[cnt]);
            cnt++;
        }
        for(int j=i*i;j<edge&&j>=0;j=j+i)
        {
            prime[j]=1;
           // printf("i=%d j=%d i*j=%d\n",i,j,i*j);
        }
    }

}
