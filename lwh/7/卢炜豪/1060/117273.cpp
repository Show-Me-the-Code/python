#include<stdio.h>
int main()
{
    char c;
    while(scanf("%c",&c)!=EOF)
    {
        if(c>=97&&c<=122)
        {
            c=c-32;
        }
        else c=c;
        printf("%c",c);
    }
}
