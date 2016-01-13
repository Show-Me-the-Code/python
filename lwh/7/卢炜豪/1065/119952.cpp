#include<stdio.h>
#include<string.h>
int main()
{
    char c,s[1025];
    while(scanf("%c",&c)==1)
    {
        getchar();
        gets(s);
        int l=strlen(s);
        for(int i=0;i<l;i++)
        {
            if(s[i]!=c)
                printf("%c",s[i]);
        }
        printf("\n");
    }
}
