#include<stdio.h>
void move(int n,char a,char b,char c);
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
         move(n,'a','b','c');
         printf("\n");
    }
}
void move(int n,char a,char b,char c)
{
    if(n==1)
        printf("%c-->%c\n",a,c);
    else
    {
        move(n-1,a,c,b);
        printf("%c-->%c\n",a,c);
        move(n-1,b,a,c);
    }
}
