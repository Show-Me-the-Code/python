#include<stdio.h>
#include<math.h>
int main()
{
    double ar,ai,br,bi;
    while(scanf("%lf %lf %lf %lf",&ar,&ai,&br,&bi)!=EOF)
    {
        double u,v,w,x,y,z;
        u=ar+br;
        v=ai+bi;
        w=ar*br-ai*bi;
        x=ai*br+ar*bi;
        y=(ar*br+ai*bi)/(pow(br,2)+pow(bi,2));
        z=(ai*br-ar*bi)/(pow(br,2)+pow(bi,2));

       // printf("%.0lf %.0lf %.0lf %.0lf %0.0lf %0.0lf\n",u,v,w,x,y,z);
       // printf("%.0lf %.0lf %.0lf %.0lf %lf %lf\n",u,v,w,x,y,z);
        printf("%d %d %d %d %d %d\n",(int)u,(int)v,(int)w,(int)x,(int)y,(int)z);
    }
}
