#include<stdio.h>
#include<string.h>
#define maxn 105
int main()
{
    char s[maxn];
    while(scanf("%s",s)!='\0')
    {
        int count=0;
        int len=strlen(s);
        for(int i=0;i<len;i++)

        if(s[i]>=65&&s[i]<=90)
                count++;
        for(int i=0;i<len;i++)
            printf("%c",s[i]);

        for(int i=0;i<count;i++)
            printf("!");
            printf("\n");

    }


}
