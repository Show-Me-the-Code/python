#include<stdio.h>
#include<string.h>
int main()
{
    char comet[10],earth[10];
    while(scanf("%s %s",comet,earth)!=EOF)
    {
        long long int add1=1,add2=1;
        int len1=strlen(comet);
        int len2=strlen(earth);

        for(int i=0;i<len1;i++)
        add1=add1*(comet[i]-'A'+1);
        for(int i=0;i<len2;i++)
        add2=add2*(earth[i]-'A'+1);



        long long int last1=add1 % 47;
        long long int last2=add2 % 47;
        if(last1==last2)
            printf("Go\n");
        else printf("STAY\n");
    }

}
