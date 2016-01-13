#include<stdio.h>
int main()
{
    double n;double k;
    while(scanf("%lf %lf",&n,&k)!=EOF)
    {
        double price=200;int s=n;
        int year=1;
        while(s<price)
        {

            s=s+n;
            price=price*((k/100)+1);
     //       printf("pricr=%lf s=%d\n",price,s);
            year++;
            if(year>=21) break;

        }



           if(year<21) printf("%d\n",year);
           else printf("Impossible\n");
      ;
    }
}
