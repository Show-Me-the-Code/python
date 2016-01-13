#include<stdio.h>
#include<string.h>
int main()
{
    int n;char a[1005],c[1005],b[1005];
    scanf("%d",&n);
    getchar();
    gets(c);
    for(int i=1;i<n;i++)
    {
        gets(a);

        if(strcmp(a,c)<0)
        {
            strcpy(b,c);
            strcpy(c,a);
            strcpy(a,b);
        }

    }
    puts(c);
}
