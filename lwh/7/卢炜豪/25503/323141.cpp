#include <cstdio>
#include <algorithm>
using namespace std;
struct Cow
{
	long long int height;
	long long int weight;
	long long int strength;
	double rate;
}cow[25];
int cmp(const void *a,const void *b)
{
	return ((*(Cow *)a).rate < (*(Cow *)b).rate) ? 1 : -1;
}
int main()
{
	long long int N,H,L=0,ans=0;
	scanf("%lld %lld",&N,&H);

	for(int i=1 ; i<=N; i++){
		scanf("%lld %lld %lld",&cow[i].height,&cow[i].weight,&cow[i].strength);
		if(cow[i].height >= H){
            printf("1\n");
            return 0;
		}
		cow[i].rate = cow[i].strength / (double)cow[i].weight;
		//printf("%lf\n",cow[i].rate);
	}
	qsort(cow+1,N+1,sizeof(cow[0]),cmp);

	//for(int i=1; i<=N ;i++)
		//printf("%lf\n",cow[i].rate);

	long long int Dexdown = 1,Dexup = N;
	while(L < H){
		L += cow[Dexdown].height;
		ans++;
		//printf("%lld\n",L);
		for(int i=Dexup; i>=1; i--){
			if(L+cow[Dexup].height >= H){
                L += cow[Dexup].height;
				ans++;
				//Dexup--;
				break;
			}
		}
		Dexdown++;
	}
	printf("%lld\n",ans);

}
