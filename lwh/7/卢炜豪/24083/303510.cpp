#include <cstdio>
#include <algorithm>
int main()
{
    int N,a[10000+2];
    scanf("%d",&N);
    for(int i=1;i<=N;i++)
        scanf("%d",&a[i]);
    std::sort(a,a+N+1);
    printf("%d\n",a[(N+1)/2]);
}
