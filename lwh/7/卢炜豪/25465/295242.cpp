#include <cstdio>
#include <cmath>
int main()
{
    int n;scanf("%d",&n);
    int i=1;
    while(i<=n)
    {
        int count=0;
        char num[13];
        scanf("%s",num);
        if(num[0]!='X')
        {
         //   printf("!\n");
            for(int j=0;j<11;j++)
            {
                if(num[j]=='X')
                    count++;
            }
        //    printf("%d\n",count);
            printf("Case #%d: %.0lf\n",i,pow(10,count));
        }
        else if(num[0]=='X')
        {
            for(int j=1;j<11;j++)
            {
                if(num[j]=='X')
                    count++;
            }
            printf("Case #%d: %.0lf\n",i,9*pow(10,count));

        }
        i++;
    }
}
