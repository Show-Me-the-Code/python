#include <cstdio>
#include <cmath>
#include <cstring>
int main()
{
    int T;
    scanf("%d",&T);
    while(T)
    {
        int n,count=0;
        char ss[18];
        scanf("%d",&n);
        int l=0;
        char s[6];
        scanf("%s",s);
        strcpy(ss,s);
        int len=strlen(s)-1;
        l=l+len;
        n=n-1;
        while(n)
        {
            scanf("%s",s);
            strcat(ss,s+1);
            len=strlen(s)-1;
            l=l+len;
            n--;
        }
    //    printf("l==%d\n",l);
    //    printf("%s",ss);
        if(l<=8)
        {
            if(l<8)
                printf("AC\n");
            if(l==8)
            {
                for(int i=0;i<=l;i++)
                {
                    if(ss[0]=='1'||(ss[i]=='0'&&i!=0))
                        count++;
                }
     //          printf("count=%d\n",count);
                if(count==9)
                    printf("AC\n");
                else
                    printf("TLE\n");
            }


        }
        if(l>8)
            printf("TLE\n");
        T--;
    }
}
