#include<stdio.h>

#include<string.h>

int main()
{
    char c[1024];
    while(gets(c)!='\0')
    {
        int l;int t=0;
        l=strlen(c);
       // printf("%d\n",l);

            for(int m=0,n=l-1;m<=n;m++,n--)
            {
                if(c[m]==c[n])
                    t++;
            }
            if(t==(l/2)||(t==(l+1)/2)) printf("Yes\n");
            else if(t!=(l/2)) printf("No\n");


    }
    return 0;
}
