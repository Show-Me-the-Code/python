#include <cstdio>
#include <cmath>
#include <cstring>
int main()
{
    int T;
    scanf("%d",&T);
    while(T)
    {
        int n;
        scanf("%d",&n);
        int l=0;
        long long int num=1;
        while(n)
        {
            char s[6];
            scanf("%s",s);
            int len=strlen(s)-1;
            l=l+len;
            n--;
        }
        if(l<=8)
        {
           // if(l<=8)
                printf("AC\n");


        }
        if(l>8)
            printf("TLE\n");
        T--;
    }
}
