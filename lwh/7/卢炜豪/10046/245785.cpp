#include<stdio.h>
#include<math.h>
long long int  sum(int n);
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
    long long int last=sum(n);
    printf("%lld\n",last);
    }
}
long long int sum(int n)
{
    long long int cn;
    if(n==1)
        cn=3;
    else
    cn=2+pow(2,n)+sum(n-1);

    return cn;

}
