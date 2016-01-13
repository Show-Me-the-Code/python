#include<stdio.h>
#include<string.h>
#define maxn 100005
int main()
{
    int n;
    scanf("%d",&n);
    getchar();
    for(int p=0;p<n;p++)
    {
        char a[maxn],b[maxn],c[maxn],d[maxn];int count=0;
        gets(a);
        int m=strlen(a);
        gets(b);
        int n=strlen(b);

        int k=0;
        for(int i=0;i<m;i++)
        {
            if(a[i]!=' ')
            {
                c[k]=a[i];
                k++;
            }
        }
        int h=0;
        for(int j=0;j<n;j++)
        {
            if(b[j]!=' ')
            {
                d[h]=b[j];
                h++;
            }
        }
        if(h==k)
        {
            for(int j=0;j<h;j++)
            {
                if(c[j]==d[j])
                    count++;
            }
            if(count==h)
                printf("equal\n");
            else if(count!=h)
                printf("not equal\n");
        }
        if(h!=k)
            printf("not equal\n");

    }
}
