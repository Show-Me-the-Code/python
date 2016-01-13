#include<stdio.h>
#include<string.h>
#define data 105
int main()
{
    char c[data],v[data];
    while(gets(c))
    {
        int l=strlen(c);
        int temp;int i,t;
        for(t=0;t<l;t++){v[t]=c[t];}
        for(i=1;i<l;i++)
        {
            if(c[i]>c[i-1]) c[i]=c[i];
            else if(c[i]<c[i-1]){ c[i]=c[i-1];}
          // printf("%c\n",c[l-1]);

        }
        char w=c[l-1];
        for(int p=0;p<l;p++)
        {
            if(v[p]==w)
                printf("%c(max)",v[p]);
            else if(v[p]!=w)
                printf("%c",v[p]);
        }
        printf("\n");


    }
}
