#include<stdio.h>
#define maxn 100000
int main()
{
int a[maxn]={0},N,M,Q,ai,bi,ci,di,ei;
while(scanf("%d",&N)==1)
{
int f=1;
if(N==0) break;
scanf("%d %d",&M,&Q);
for(int i=0;i<M;i++)
{
scanf("%d %d %d",&ai,&bi,&ci);
for(int j=ai;j<=bi;j++)
a[j]=a[j]+ci;
}

for(int i=0;i<Q;i++)
{
scanf("%d %d",&di,&ei);
long long int sum=0;
for(int j=di;j<=ei;j++)
sum=sum+a[j];
printf("%lld\n",sum);
}
}
}
