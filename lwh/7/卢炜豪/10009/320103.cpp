#include <cstdio>
#include <cmath>
double f(double x); //计算f(x)的值
double y;			//把题目中的y设成全局变量
using namespace std;
int main()
{
    while(scanf("%lf",&y)!=EOF)
    {
        double x,a=-200,b=200,end=0.001;  //因为fabs(y)<=7000000,也就意味着x值的范围会在(-200,200)的范围内。a,b分别表示区间的左右端点
        while(1)
        {
			//f(a)*f(b)是依据二分法的定义。这里加上等于0的情况可以在后面节省掉一种讨论（题目一定有解，所以不存在任意f(a)*f(b)大于0的情况）
            if(f(a)*f(b)<=0)            
            {
                if(f(a)==0)             //如果f(a)==0,说明a就是答案
				{
					printf("%.3lf\n",a);
					break;
				}
				else if(f(b)==0)      //同理 ↑  
				{
					printf("%.3lf\n",b);
					break;
				}			
                else if(f(a)*f(b-(b-a)/2)<0)  //这里是把区间进行二分，b-(b-a)/2才是二分后端点坐标的正确表达式
                {
                    a=a;
                    b=b-(b-a)/2;
                }
                else if(f(b-(b-a)/2)*f(b)<0) //同 ↑
                {
                   a=b-(b-a)/2;
                   b=b;
                }
				
				//当区间很接近的时候，其实a或者b都可以认为是答案（只要超过要保留的位数就行，比如3.1412,3.1413,保留三位小数都是3.141）
                if(fabs(f(a))<=end) 
                {
                printf("%.3lf\n",a);
                break;
                }
            }
             //   printf("3\n");
        }


    }
    return 0;
}
double f(double x)
{
    double fx=3*x*x*x+2*x;
    return fx;
}
