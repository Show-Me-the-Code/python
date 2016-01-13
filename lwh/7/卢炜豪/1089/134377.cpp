#include<stdio.h>
int main()
{
    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
    {
        int a,b,total=0;char c;
        scanf("%d%c%d",&a,&c,&b);
      //  getchar();
        if(c=='+') total=a+b;
        else if(c=='-') total=a-b;
        else if(c=='*') total=a*b;
        else if(c=='/') total=a/b;
        c=getchar();
        int d;
        for(;c!='=';)
        {
            scanf("%d",&d);
            if(c=='+')
                total=total+d;
            else if(c=='-')
                total=total-d;
            else if(c=='*')
                total=total*d;
            else if(c=='/')
                total=total/d;
            c=getchar();
        }
        printf("%d\n",total);
    }
}
