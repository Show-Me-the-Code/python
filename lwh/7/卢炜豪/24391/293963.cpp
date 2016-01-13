#include <cstdio>
int main()
{
    int num,QA,a[1200000+5],st=0;
    scanf("%d %d",&num,&QA);
    for(int i=1;i<=num;i++)
    {
        int len;
        scanf("%d",&len);
        len=len+st;
        int temp=len;
        while(len>=st&&len>0)
        {
            a[len]=i;
         //   printf("len=%d\n",len);
            len--;
        }
        st=temp;
        a[0]=1;
    }
    for(int i=0;i<QA;i++)
    {
        int where;
        scanf("%d",&where);
        printf("%d\n",a[where]);
    }
}
