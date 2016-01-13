#include<stdio.h>
#include<string.h>
int main()
{
    char s[105];
    while(gets(s)!='\0')
    {
        int l=strlen(s);
        printf("%c",s[0]-32);
        for(int i=1;i<l;i++)
        {
            printf("%c",s[i]);
        }
        printf("\n");

    }

}
