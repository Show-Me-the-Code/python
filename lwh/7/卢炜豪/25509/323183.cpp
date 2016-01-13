#include <cstdio>
#include <cmath>
using namespace std;
struct Point
{
	int x;
	int y;
}point[100005];
int main()
{
	int N,Maxl=0,Res=0;
	scanf("%d",&N);
	for(int i=1 ; i<=N ; i++){
		scanf("%d %d",&point[i].x,&point[i].y);
	}

	for(int i=2; i<=N ; i++){
		Maxl += fabs(point[i].x-point[i-1].x)+fabs(point[i].y-point[i-1].y);
	}
	//printf("Maxl=%d\n",Maxl);

	int temp,Min=Maxl;
	for(int i=2; i<=N-1 ; i++){
		int dis_a = fabs(point[i].x-point[i-1].x)+fabs(point[i].y-point[i-1].y);
		int dis_b = fabs(point[i+1].x-point[i].x)+fabs(point[i+1].y-point[i].y);
		int dis_cut = dis_a + dis_b;
		int dis_add = fabs(point[i+1].x-point[i-1].x)+fabs(point[i+1].y-point[i-1].y);
		Res = Maxl - dis_cut + dis_add;
		//printf("dis_cut=%d dis_add=%d Res=%d\n",dis_cut,dis_add,Res);
		if(Min > Res)
			Min = Res;
	}
	printf("%d\n",Min);
}
