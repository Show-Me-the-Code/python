#include <cstdio>
#include <cstring>
#include <cmath>
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        int N,m;
        int in[200000+5];
        char s[200000+5];
        long long int sum=0;
        scanf("%d %d",&N,&m);
        getchar();
        gets(s);
        int len=strlen(s),i,v;
        for(i=0,v=0;i<len;i++)
        {
            if(s[i]!=' ')
            {
                in[v]=s[i]-48;
                v++;
                //printf("%d",in[v]);
            }
        }
        for(int z=0;v>=0;v--,z++)
            sum=sum+in[v];
      //  printf("sum=%lld m=%d sum%m=%d\n",sum,m,sum%m);
      if(sum%m==0)
        printf("Stay here\n");
      else
        printf("I will go with you\n");
    }
}
