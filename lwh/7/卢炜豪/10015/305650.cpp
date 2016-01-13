#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int gcd(int a,int b);
int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n)!=EOF)
    {
        int temp=0;
        int j=m,k=n;
        if(m>=n)
        {
            temp=m/n;
            m=m-n;
        }
        int r=gcd(m,n);
        m/=r;n/=r;
        if(j==0)
        printf("0\n");
        else
        {

        if(temp!=0&&j%k==0)
            printf("%d\n",j/k);
        if(temp!=0&&j%k!=0)
            printf("%d %d/%d\n",temp,m,n);
        else if(temp==0)
            printf("%d/%d\n",m,n);
        }

    }
}
int gcd(int a,int b)
{
  //  int temp=a%b;
    while(b!=0)
    {
        int t=a;
        a=b;
        b=t%b;
       // temp=b;
    }
    //printf("b=%d\n",a);
    return a;
}
