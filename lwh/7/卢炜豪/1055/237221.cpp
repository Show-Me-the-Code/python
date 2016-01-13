#include<stdio.h>
struct book
{
    int price;
    char name[65];
};
int main()
{
    int n;
    while(scanf("%d",&n)==1&&n!=0)
    {
        struct book a[10000];
        for(int i=0;i<n;i++)
        {
            scanf("%s %d",a[i].name,&a[i].price);
        }
        int max=a[0].price,min=a[0].price;
        for(int i=0;i<n;i++)
        {
            if(a[i].price>max)
                max=i;
            if(a[i].price<min)
                min=i;
           // printf("max=%d,min=%d\n",max,min);
        }
      //  printf("max=%d,min=%d\n",max,min);
        printf("%s %s\n",a[max].name,a[min].name);
    }
}
