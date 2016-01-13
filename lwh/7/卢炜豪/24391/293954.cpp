#include <cstdio>
int main()
{
    int num,QA,a[10000+5],st=0;
    scanf("%d %d",&num,&QA);
    for(int i=1;i<=num;i++)
    {
        int len;
        scanf("%d",&len);
        len=len+st;
        int temp=len;
        while(len>=st)
        {
            a[len]=i;
            len--;
        }
        st=temp;
    }
    for(int i=0;i<QA;i++)
    {
        int where;
        scanf("%d",&where);
        if(where==0)
            printf("1\n");
        else
        printf("%d\n",a[where]);
    }
}
