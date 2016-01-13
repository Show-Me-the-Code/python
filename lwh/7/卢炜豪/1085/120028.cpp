#include<stdio.h>
#include<string.h>
int main()
{
    char s[105];
    while(gets(s)!='\0')
    {
        int l=strlen(s);
        if(s[0]>=97&&s[0]<=122)
        printf("%c",s[0]-32);
        else printf("%c",s[0]);
        for(int i=1;i<l;i++)
        {
            if(s[i-1]==' ')
            s[i]=s[i]-32;
            else s[i]=s[i];
        }
        for(int i=1;i<l;i++) printf("%c",s[i]);
        printf("\n");
    }
}
