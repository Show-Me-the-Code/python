#include <cstdio>
#include <algorithm>
using namespace std;
int a[100+5],b[100+5];
int palindrome(int m,int n);
int main()
{
    int n,L;
    scanf("%d %d",&n,&L);
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
         sort(a,a+n);
    for(int i=0;i<n-1;i++)
    {
        b[i]=a[i+1]-a[i];
       // printf("%d\n",b[i]);
    }
    int c=0;
    for(int i=0;i<n-1;i++)
    {
        if(palindrome(0,i))
         {
            c++;
         }

    }
 //   printf("%d\n",c);
    for(int i=1;i<n-1;i++)
    {
        if(palindrome(i,n-2))
           {

            c++;
           }


    }
    printf("%d\n",c);
}
int palindrome(int m,int n)
{
    for(int i=0;i+m<=n-i;i++)
    {
//        printf("%d %d\n",b[i],b[q]);
        if(b[m+i]!=b[n-i])
            return 0;
    }
    return 1;
}
