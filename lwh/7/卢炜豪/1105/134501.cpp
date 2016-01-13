#include<stdio.h>
#include<math.h>
int main()
{
   double a,b,c;
   while(scanf("%lf %lf %lf",&a,&b,&c)!=EOF)
   {
        if((b*b-4*a*c)<0) printf("none\n");
        else if(b*b-4*a*c==0)
        {
            if(((-b)/2*a)==0)
            printf("0.00\n");
            else printf("%.2lf\n",((-b)/2*a));
        }
        else if(b*b-4*a*c>0)
        {
            double m,n;
            m=((-b)+(sqrt(b*b-4*a*c)))/(2*a);
            n=((-b)-(sqrt(b*b-4*a*c)))/(2*a);
            if(m>n) printf("%.2lf %.2lf\n",n,m);
            else printf("%.2lf %.2lf\n",m,n);
        }
   }
}
