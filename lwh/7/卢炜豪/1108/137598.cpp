#include<stdio.h>
#define maxn 9999
int main()
{
    int people;
    while(scanf("%d",&people)!=EOF)
    {
        int a[maxn];

        for(int i=0;i<people;i++)
        {
            scanf("%d",&a[i]);
        }
        int temp;
        for(int i=1;i<people;i++)
        {
            for(int j=0;j<people-i;j++)
            {
                if(a[j]>a[j+1])
                {
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }
        printf("%d\n",a[people-1]);
    }
}
