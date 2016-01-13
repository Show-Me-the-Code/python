#include<stdio.h>
int main()
{
    char a[1005],b[1005];int t=0,q=0;
    for(int i=0;i<1005;i++)
    {
        a[i]=getchar();
        b[i]=getchar();

    }
    for(int i=0;i<1005;i++)
    {
        if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u') t++;
        if(b[i]=='a'||b[i]=='e'||b[i]=='i'||b[i]=='o'||b[i]=='u') q++;
    }
    if(q>t) printf("a>b\n");
    if(q==t) printf("a=b\n");
    if(q<t) printf("a<b\n");
}
