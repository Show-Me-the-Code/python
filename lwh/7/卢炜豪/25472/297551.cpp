#include <cstdio>
#include <cstring>
int main()
{
    int T,q=1;
    scanf("%d",&T);
    while(q<=T)
    {
        char s[1000+5];int a[1000+5],k;
        scanf("%s %d",s,&k);
        int k1=k;
        for(int i=0;i<strlen(s);i++)
            a[i]=s[i]-48;
        int min=11,start=0,count=0,index,left=strlen(s)-k;
        printf("Case #%d: ",q);
        while(1)
        {
            for(int i=start;i<=start+k;i++)
                if(a[i]<min)
                   {
                       min=a[i];
                       index=i;
                   }
            if(min!=0)
            printf("%d",min);
            break;
            min=11;
            start=index+1;
            k--;

        }
        for(int i=k1+1;i<=left+1;i++)
            printf("%c",s[i]);
        printf("\n");
        q++;
    }
}
