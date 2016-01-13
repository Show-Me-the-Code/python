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
    for(int kkk=1;kkk<=T;kkk++)
    {
        char k[11];
        int n,a[11];
        scanf("%s %d",k,&n);
        int l=strlen(k);

        for(int i=0;i<l;i++)
            a[i]=k[i]-48;
            printf("Case #%d: ",kkk);
        int start_point=0,index,count=0,p=1;
        for(int i=start_point;i<l;)
        {
            int max=11;
            for(int j=i;j<n+p;j++)
            {
                if(a[j]<max)
                {
                    max=a[j];
                    index=j;
                }
            }
            count++;
            if(i==0)
            {
                if(max!=0)
                    printf("%d",max);
            }
            else
            printf("%d",max);

            if(count==l-n)
                break;

             p++;
            i=index+1;
        }
        printf("\n");

    }
    return 0;
}
