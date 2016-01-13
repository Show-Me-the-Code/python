#include<stdio.h>
#include<string.h>
int main()
{
    char s[130];int d=0;
    while(gets(s)!='\0')
    {
        int l=strlen(s);
        int space=0;
       // printf("l=%d\n",l);
        for(int i=0;i<l;i++)
        {
            if(s[i]==' ') space++;
        }
        if(space==0)
        {
            for(int i=0;i<l;i++) printf("%c",s[i]);

        }
        else if(space!=0)
        {
            for(int i=l;i>0;i--)
            {
                if(s[i-1]==' ')
                {
                   d=i;
                   break;
                }
            }

        //printf("%d\n",d);
        for(int q=d;q<l;q++)
        {
            printf("%c",s[q]);
        }
        }
        printf("\n");

    }
}
