#include<stdio.h>
#include<string.h>
#include<math.h>
#define maxn 11
int main()
{
    char k[maxn];int n,p=0;
    while(scanf("%s %d",k,&n)==2)
    {
        if(k[0]-'0'==0&&n==0) break;
        int len=strlen(k);
        int left=len-n,x=left-1,l;//left存储剩下的位数  x表示去掉的个数
        int max=k[0]-'0',index;
        for(int i=0;i<=n;i++)
        if(k[i]-'0'>max)
        {max=k[i]-'0';}
        int w=0;
        for(int i=0;i<len-1;i++)
        {
            if(k[i]-'0'==k[i+1]-'0')
                w++;
        }
        if(w==len)
        {
            for(int i=0;i<left;i++) printf("%c",k[i]);
            printf("\n");
        }
        for(l=0;l<len;l++)
        {
            if(k[l]-'0'==max)
                {index=l;break;}
        }
    //    printf("max=%d index=%d n=%d\n",max,index,n);
        if(index==n)
        {
            for(int i=index;i<len;i++)
                printf("%c",k[i]);
            printf("\n");
        }
        //ok,前面为止都是在考虑特殊情况，一下开始进行正常情况编写
        if(index!=n)
        {
            //因为第一个最大值已经得到，且不用考虑那个特殊情况，所以直接求接下来每次循环中的最大值
            int p=0;
            for(;x>=0;)
            {
                p=p+max*pow(10,x);//printf("x=%d\n",x);
                max=k[l+1]-'0';
                for(int i=index+1;i<len;i++)
                {
                    if(k[i]-'0'>max)
                        max=k[i]-'0';
                }
                 for(int l=0;l<len;l++)
                {
                 if(k[l]-'0'==max)
                {index=l;break;}
                }
             //   printf("max==%d\n",max);
                index++;
                x--;
            }
            printf("%d\n",p);

        }
    }
}
