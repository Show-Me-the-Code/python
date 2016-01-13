/*
    思路先明确下吧：假如要去掉k个数，就每次以k个数字为一组，
    筛出最大的一个。下次筛选就以筛出的最大的那个数后面加1的k个数为一组
*/
#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        char k[1005];
        int n,a[1005],b[1005],v=0;
        scanf("%s %d",k,&n);
        int l=strlen(k);

        if(k[0]=='0'&&n==0)
            break;

        for(int i=0;i<l;i++)
            a[i]=k[i]-48;

        int start_point=0,index,count=0,p=1;
        for(int i=start_point;i<l;)
        {
            int min=11;
            for(int j=i;j<n+p;j++)
            {
                if(a[j]<min)
                {
                    min=a[j];
                    index=j;
                }
            }
            count++;
            b[v]=min;
            v++;
           // printf("%d",min);

            if(count==l-n)
                break;

             p++;
            i=index+1;
        }
        for(int mn=0;mn<v;mn++)
        {
            if(mn==0)
            {
                if(b[mn]!=0)
                    printf("%d",b[mn]);
            }
            if(mn!=0)
                printf("%d",b[mn]);

        }
        printf("\n");

    }
}
