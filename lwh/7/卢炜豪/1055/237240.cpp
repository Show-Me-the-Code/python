#include<stdio.h>
struct book
{
    double price;
    char name[65];
};
int main()
{
    int n;
    while(scanf("%d",&n)==1&&n!=0)
    {
        struct book a[50000];
        for(int i=0;i<n;i++)
        {
            scanf("%s %d",a[i].name,&a[i].price);
        }
        int max=0,min=0;
        for(int i=1;i<n;i++)
        {
            if(a[i].price>a[i-1].price)
                max=i;
            if(a[i].price<a[i-1].price)
                min=i;
           // printf("max=%d,min=%d\n",max,min);
        }
      //  printf("max=%d,min=%d\n",max,min);
        printf("%s %s\n",a[max].name,a[min].name);
    }
}
