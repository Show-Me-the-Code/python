#include<stdio.h>
#include<string.h>
int main()
{
    char s[205];
    while(gets(s)!='\0')
    {
        int l=strlen(s);
        int l1=strlen(s);
        if(l==3)
        {
            if(s[0]=='E'&&s[1]=='N'&&s[2]=='D')
            break;

        }

        for(int i=0;i<l1;i++)
        {

        if(s[i]=='A'||s[i]=='W'||s[i]=='F')
        printf("I");
        else if(s[i]=='C')
        printf("L");
         else if(s[i]=='M')
                printf("o");
                else if(s[i]=='S')
                printf("v");
                else if(s[i]=='D'||s[i]=='P'||s[i]=='G'||s[i]=='B')
                printf("e");
                else if(s[i]=='L')
                printf("Y");
                else if(s[i]=='X')
                printf("u");
                else printf("%c",s[i]);
            }
            printf("\n");
        }

    }
