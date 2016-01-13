#include<stdio.h>

#include<string.h>

#define maxn 1005

int main()

{

    char s[maxn],ch;

    int i=0;

    while(gets(s)!='\0')

    {

       // gets(s);

        ch=getchar();

        int num=-1;

        int l=strlen(s);

        for(int i=0;i<l;i++)

        {

            if(s[i]==ch)

            {

                num=i;

                break;

            }

        }

        if(num==-1)

        {

            printf("Not Found\n");



        }

        else

        {

        for(int i=num;i<l;i++) printf("%c",s[i]);

        printf("\n");



        }
        getchar();

    }

}
