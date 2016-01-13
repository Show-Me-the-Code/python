#include<stdio.h>
int main()
{
    int n;double sum;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        sum=1;int day;
        scanf("%d",&day);
        for(int j=1;j<day;j++)
            sum=2*sum+2;
                printf("%.0lf\n",sum);
    }
    

}
