#include<stdio.h>
int main()
{
    char c;
    while(scanf("  %c",&c)!=EOF)
    {
        if(c>='a'&&c<='z')
{
            c=c-32;
            printf("%c\n",c);
}
       else printf("%c\n",c);
}
    return 0;
}
