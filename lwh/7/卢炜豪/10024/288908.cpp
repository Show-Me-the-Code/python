#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
int main()
{
    int n;
    double p1=sqrt(5);
    double p2=1/sqrt(5);
  //  printf("%lf %lf\n",p1,p2);
    while(scanf("%d",&n)!=EOF)
    {
       double result=p2*pow(((1+p1)/2),n)-p2*pow(((1-p1)/2),n);
       printf("%.0lf\n",result);
    }
}
