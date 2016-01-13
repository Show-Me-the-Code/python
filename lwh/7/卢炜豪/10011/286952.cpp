#include <stdio.h>

struct price
{
    int n;double v;

    double oneprice;

};
int main()
{
    int w,s;struct price p[105];
    while(scanf("%d %d",&w,&s)!=EOF)
    {
        for(int i=0;i<s;i++)
        {
            scanf("%d %lf",&p[i].n,&p[i].v);
            p[i].oneprice=p[i].v/p[i].n*1.0;
       //     printf("%lf\n",p[i].oneprice);

        }

        for(int i=1;i<s;i++)
        {
            for(int j=0;j<s-i;j++)
            {
                if(p[j].oneprice<p[j+1].oneprice)
                {

                    double temp=p[j].oneprice;
                    p[j].oneprice=p[j+1].oneprice;
                    p[j+1].oneprice=temp;

                    int m=p[j].n;
                    p[j].n=p[j+1].n;
                    p[j+1].n=m;

                }
            }
        }

    //    for(int i=0;i<s;i++)
     //   printf("%lf %d\n\n",p[i].oneprice,p[i].n);

        double maxv=0;

        for(int i=0;w>0;i++)
        {
            if(p[i].n>=w)
            {
             //   printf("p[%d].oneprice=%lf w=%d maxv=%lf\n",i,p[i].oneprice,w,maxv);
                maxv=p[i].oneprice*w+maxv;
               // printf("%lf\n",maxv);
                break;
            }
            else
            {
                maxv=p[i].oneprice*p[i].n+maxv;
               // printf("%lf\n",maxv);
                w=w-p[i].n;
               // printf("w=%d\n",w);
            }

        }

        printf("%.2lf\n",maxv);

    }
}
