#include<stdio.h>
#include<string.h>
int main()
{
    int n,i,j,k;
    scanf("%d",&n);
    getchar();
    for(i=0;i<n;i++)
    {
        k=0;
        //getchar();
        char s[55];int count=0;
        gets(s);
        int l=strlen(s);
       // printf("l=%d\n",l);
        if((s[0]>=65&&s[0]<=90)||(s[0]>=97&&s[0]<=122)||s[0]=='_')
            k=1;
        else if(s[0]>='0'&&s[0]<='9')  k=0;
        else k=0;
       // printf("k=%d\n",k);
        if(k==0) printf("no\n");
        else if(k==1)
        {

        for(j=1;j<l;j++)
        {
            if((s[j]>=65&&s[j]<=90)||(s[j]>=97&&s[j]<=122)||s[j]==95||s[j]=='_'||(s[j]>='0'&&s[j]<='9' ))
                count++;
        }
    //    printf("l=%d i=%d\n",l,j);
        if(count==l-1)
            printf("yes\n");
        else printf("no\n");

        }
        }

    }

