#include<stdio.h>
int main()
{
    int year;
    while(scanf("%d",&year)!=EOF)
    {
        if(year%4==0&&year%100!=0) printf("yes\n");
        else if(year%400==0) printf("yes\n");
        else printf("no\n");
    }

}
