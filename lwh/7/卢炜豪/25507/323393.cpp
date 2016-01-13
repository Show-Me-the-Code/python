#include <cstdio>
#include <cmath>
using namespace std;
int book[100005];
int N,K;
struct Point
{
	int x;
	int y;
}point[100005];
int cut(int Maxl,int K)
{
   // printf("Maxl=%d K=%d\n",Maxl,K);
    int Res,Min=Maxl;
    if(K==1)
        return Min;
    //int Res,Min=Maxl;
	for(int i=2; i<=N-1 ; i++){
        if(book[i]==0){
            int dis_a = fabs(point[i].x-point[i-1].x)+fabs(point[i].y-point[i-1].y);
            int dis_b = fabs(point[i+1].x-point[i].x)+fabs(point[i+1].y-point[i].y);
            int dis_cut = dis_a + dis_b;
            int dis_add = fabs(point[i+1].x-point[i-1].x)+fabs(point[i+1].y-point[i-1].y);
            Res = Maxl - dis_cut + dis_add;
            book[i]=1;
            if(Min > Res)
                Min = Res;
            cut(Res,K-1);
        }
	}

	return Min;
}
int main()
{
	int Maxl=0;
	//freopen("test.in","r",stdin);
	scanf("%d %d",&N,&K);
	//算出都走一遍的长度
	for(int i=1 ; i<=N ; i++){
		scanf("%d %d",&point[i].x,&point[i].y);
		if(i>=2){
        Maxl += fabs(point[i].x-point[i-1].x)+fabs(point[i].y-point[i-1].y);
		}
	}
	printf("%d\n",cut(Maxl,K));
}
