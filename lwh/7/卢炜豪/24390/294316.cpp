#include <cstdio>
#include <cmath>
double distance(double m,double n,double m1,double n1);
struct x_y
{
    double x;
    double y;
    double dis;
    int index;
};
int main()
{
    int N;struct x_y s[500+2];
    scanf("%d",&N);
    for(int i=1;i<=N;i++)
    {
        scanf("%lf %lf",&s[i].x,&s[i].y);
        s[i].index=i;
    }
    double max=0;int k=0;
    for(int i=1;i<=N;i++)
    {
        for(int j=0;j<=i;j++)
        {
            s[i].dis=distance(s[i].x,s[i].y,s[j].x,s[j].y);
         //   printf("dis[%d]=%lf\n",i,s[i].dis);
            if(s[i].dis>max)
                max=s[i].dis;
                k++;
        }
    }
    int i,j;
     for(i=1;i<=N;i++)
    {
        for(j=0;j<=i;j++)
        {
            double dis0=distance(s[i].x,s[i].y,s[j].x,s[j].y);
            if(dis0==max)
            {
                if(j>i)
                    printf("%d %d\n",i,j);
                else
                    printf("%d %d\n",j,i);
                break;
            }
        }
    }

}
double distance(double m,double n,double m1,double n1)
{
    double dis=sqrt(pow(fabs(m-m1),2)+pow(fabs(n-n1),2));
    return dis;
}
