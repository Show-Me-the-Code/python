#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
int FindNext(int n,int choose);
int a[1001],M,v;
int main()
{
    a[1]=1;a[2]=2;a[3]=3;a[4]=4;a[5]=5;
    int n,max_index=5;v=6;
    while(v<=1001)
    {
        M=a[max_index];
        int nextback2=FindNext(M,2)*2;
        int nextback3=FindNext(M,3)*3;
        int nextback5=FindNext(M,5)*5;
        int min1=min(nextback2,nextback3);
        int min2=min(min1,nextback5);
        a[v]=min2;
        max_index++;
      //  printf("a[%d]=%d\n",v,a[v]);
        v++;

    }
    //for(int i=1;i<=1200;i++)
        //printf("%d\n",a[1500]);
    while(scanf("%d",&n)!=EOF)
    {
        printf("%d\n",a[n]);
    }
}
int FindNext(int n,int choose)
{
    if(choose==2)
    {
        for(int i=1;i<=v;i++)
        {
            if(a[i]>M/2)
                return a[i];
        }
    }
    if(choose==3)
    {
        for(int i=1;i<=v;i++)
        {
            if(a[i]>M/3)
                return a[i];
        }
    }
    if(choose==5)
    {
        for(int i=1;i<=v;i++)
        {
            if(a[i]>M/5)
                return a[i];
        }
    }
}
