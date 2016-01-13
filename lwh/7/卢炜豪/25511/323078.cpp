#include <cstdio>
#include <algorithm>
using namespace std;
struct Cow
{
	long long int s;
	long long int l;
	double time;
}cow[100005];
int main()
{
	long long int N,A[100005];
	scanf("%lld",&N);

	for(int i=1; i<=N ; i++){
		scanf("%lld %lld",&cow[i].l,&cow[i].s);
	}

	double maxtime = 0;
	for(int i=1; i<=N-1 ; i++){
		cow[i].time = (cow[i+1].l - cow[i].l) / (cow[i].s - cow[i+1].s);
		if(maxtime < cow[i].time)
            maxtime = cow[i].time;
	}
	//printf("%lf\n",maxtime);
	long long int T = (long long int)(maxtime+1);
	//printf("%lld\n",T);
	T = 10000000000;
	for(int i=1; i<=N ; i++){
		A[i] = cow[i].s * T + cow[i].l;
	}

	long long int temp = A[N];
	long long int ans = 1;
	for(int i=N ; i>0 ; i--){
		if(A[i] < temp){
			ans++;
			temp = min(A[i],temp);
		}
	}

	printf("%lld\n",ans);

}
