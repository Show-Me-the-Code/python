#include <stdio.h>
#include <math.h>
double cal(double x,double y,double x1,double y1);
struct xy
{
    double x;
    double y;
    double distance;
};
int main()
{
    int N;struct xy s[500+2];
    double a[502][502];
    scanf("%d",&N);
    for(int k=0;k<N;k++)
        scanf("%lf %lf",&s[k].x,&s[k].y);
        double max=0;
    for(int i=0;i<N-1;i++)
    {
        for(int j=i+1;j<N;j++)
        {
            a[i][j]=cal(s[i].x,s[i].y,s[j].x,s[j].y);
           // printf("%lf\n",a[i][j]);
            if(cal(s[i].x,s[i].y,s[j].x,s[j].y)>max)
                max=cal(s[i].x,s[i].y,s[j].x,s[j].y);
        }
    }
   // printf("%lf\n",max);
   for(int i=0;i<N-1;i++)
    for(int j=i+1;j<N;j++)
   {
       if(a[i][j]==max)
       {
        printf("%d %d\n",i+1,j+1);
        break;
       }
   }

}
double cal(double x,double y,double x1,double y1)
{
    double dis=pow(fabs(x-x1),2)+pow(fabs(y-y1),2);
//    printf("%lf %lf %lf %lf\n",x,y,x1,y1);
    return dis;
}
