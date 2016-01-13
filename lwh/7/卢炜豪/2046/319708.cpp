#include <cstdio>
#define max_n 100000
int main()
{
	int pos = 0,ans = 0, n, k, tank,loc[max_n];

	scanf("%d %d",&n,&k);
	tank = n;

	for(int i = 0;i <= k;i++){
		scanf("%d",&loc[i]);
	}

	int sum = 0;
	for(int i = 0;i <= k;i++){
		tank -= loc[i];
		if(tank < 0){
			tank += n;
			ans++;
			//printf("add fuel on %d\n",i-1);
		}
	}
	if(tank < 0){
        printf("No Solution\n");
        return 0;
	}
	printf("%d\n",ans+1);
	return 0;

}
