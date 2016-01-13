#include <cstdio>
#include <cstring>
#include <cmath>
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        char s[100];
        int a[100],q=0;
        scanf("%s",s);
        int len=strlen(s);
        int add=0;
        for(int i=len-1;i>=0;i--)
        {
            if(s[i]>='0'&&s[i]<='9')
                a[q]=s[i]-48;
            if(s[i]>='a'&&s[i]<='z')
                a[q]=s[i]-87;
            if(s[i]>='A'&&s[i]<='Z')
                a[q]=s[i]-29;
            if(s[i]=='#')
                a[q]=s[i]+27;
            if(s[i]=='$')
                a[q]=s[i]+27;
                add=add+a[q]*(int)(pow(64,q));
    //       printf("a[%d]=%d \n",q,a[q]);
           q++;
        }
        printf("%d\n",add);
    }
}
