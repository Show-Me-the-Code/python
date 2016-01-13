#include<stdio.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        if(n==0) break;
        int m,l,sum=0;
        m=n/4;l=n%4;
        //printf("m=%d l=%d\n",m,l);
        if(m==0&&l==1) sum=1;
        if(m==0&&l==2) sum=2;
        if(m==0&&l==3) sum=3;
        if(m==0&&l==4) sum=4;

        else if(m!=0)
        {
        for(int i=0;i<m;i++)
        {
            if(l==1)
            {
                int add0=0,add=0;
                add0=m+1;
                for(int t=m;t>0;t--)
                {
                    add=t*4+add;
                }
                sum=add0+add;
            }
            if(l==2)
            {
                int add0=0,add=0;
                add0=m+1;
                for(int t=m;t>0;t--)
                {
                    add=t*4+add;
                }
                sum=2*add0+add;
            }
             if(l==3)
            {
                int add0=0,add=0;
                add0=m+1;
                for(int t=m;t>0;t--)
                {
                    add=t*4+add;
                }
                sum=3*add0+add;
            }
             if(l==0)
            {
                int add0=0,add=0;
                add0=m;
                for(int t=m-1;t>0;t--)
                {
                    add=t*4+add;
                }
                sum=4*add0+add;
            }
        }
        }
        printf("%d\n",sum);
    }
}
