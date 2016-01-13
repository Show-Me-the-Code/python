#include <cstdio>
#include <cstring>
int main()
{
    char s1[100+2],s2[100+2],s3[100+2],s4[100+2];
    while(gets(s1))
    {
        int v=0;
        gets(s2);

        int len1=strlen(s1);
        int len2=strlen(s2);
        s1[len1]='\0';
        s2[len2]='\0';
        for(int i=0;i<=len1;i++)
        {
            if(s1[i]!=' ')
            {
                s3[v]=s1[i];
                if(s3[v]>='A'&&s3[v]<='Z')
                    s3[v]=s3[v]+32;
                v++;
            }

        }
       // printf("%s\n",s3);
        v=0;
         for(int i=0;i<=len2;i++)
        {
            if(s2[i]!=' ')
            {
                s4[v]=s2[i];
                if(s4[v]>='A'&&s4[v]<='Z')
                    s4[v]=s4[v]+32;
                v++;
            }

        }
       // printf("%s\n",s4);
        if(len1==len2&&len1==0)
            printf("YES\n");
        else
        {
        if(strcmp(s3,s4)==0)
            printf("YES\n");
        else
            printf("NO\n");
        }
    }
    return 0;
}
