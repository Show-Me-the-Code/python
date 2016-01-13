#include<iostream>
#include <cstdio>
using namespace std;
int get_last_num(int n, int m){
	int last_num = 0;
	for(int i = 2; i <= n; i++)
		last_num = (last_num + m) % i;
	return last_num;
}
int main()
{
    int n,x;
    while(scanf("%d %d",&n,&x)==2)
    {
        if(n==0&&x==0)
         break;
        int result = get_last_num(n, x);
        printf("%d\n",result+1);
    }


}
