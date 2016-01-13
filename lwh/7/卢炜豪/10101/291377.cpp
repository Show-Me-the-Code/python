#include <stdio.h>
#include <string.h>
#define maxn 10+2

struct gift
{
    char name[10];
    double income;
};
int main()
{
    int num;
    while(scanf("%d",&num)!=EOF)
    {
        struct gift s[maxn];
        for(int i=0;i<num;i++)
            s[i].income=0;

        for(int i=0;i<num;i++)
        {
            scanf("%s",s[i].name);
        }

        for(int i=0;i<num;i++)
        {
            char name1[10];
            double sum;int count;

            scanf("%s",name1);
            scanf("%lf %d",&sum,&count);

            for(int j=0;j<num;j++)
            {
                if(strcmp(name1,s[j].name)==0)
                {
                    s[j].income=s[j].income-(int)(sum/count)*count;
                    break;
                }
            }

            for(int j=0;j<count;j++)
            {
                char name2[10];
                scanf("%s",name2);

                 for(int k=0;k<num;k++)
                {
                    if(strcmp(name2,s[k].name)==0)
                    {
                        s[k].income=s[k].income+sum/count*1.0;
                        break;
                    }
                }
            }
        }

        for(int i=0;i<num;i++)
           {
               printf("%s ",s[i].name);
               if(s[i].income<0)
                printf("%d\n",(int)(s[i].income-0.9999));
               else
                printf("%d\n",(int)s[i].income);
           }
           printf("\n");

    }

    return 0;
}
