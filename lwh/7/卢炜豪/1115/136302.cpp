#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        int count=0;
        if(a+b>c&&a+c>b&&c+b>a&&a-c<b&&a-b<c&&b-c<a&&b-a<c&&c-a<b&&c-b<a)
            printf("yes\n");
        else printf("no\n");
    }
}
