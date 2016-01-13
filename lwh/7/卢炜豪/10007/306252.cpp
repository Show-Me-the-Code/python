/*
    思路：输入为n，用10（取倒数嘛）来除，得到余数x，存进数组中，
    以x做下标（但愿不会溢出），进行累加。用另一个数组记录除后的结果。对余数乘10，进行相同处理
    知道累加为2停下。ok let's go
*/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
using namespace std;
int div[100000+5],mod[100000+5];
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        memset(div,0,sizeof(div));
        memset(mod,0,sizeof(mod));
        int n;scanf("%d",&n);
        int v = 0,t = 10,k=n,flag=0;
        n=fabs(n);
        if(n<0)
            flag=1;
        if(100000%n==0)
        {
            while(n%10==0)
            {
                n/=10;
            }
            printf("0.%d",n);
        }
        else
        {

        while(1)
        {
            div[v] = t/n;
            v++;
            mod[t%n] ++;
           // printf("t/n = %d t%%n=%d mod=%d\n",t/n,t%n,mod[t%n]);
            if( mod[t % n ] == 2 && t/n != 0)
                break;

            t =  t%n *10;
        }
        if(flag==1)
            printf("-");
        printf("0.");
        for(int i=0 ; i < v-1;i++)
            printf("%d",div[i]);
        }
            printf("\n");
    }
}
