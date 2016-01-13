#include <cstdio>
#define max_n 100000+10
int main()
{
	int n,k,A[max_n];

	scanf("%d %d",&n,&k);
	for(int i = 1;i <= k + 1;i++ ){
		scanf("%d",&A[i]);

		if(A[i] > n){
			printf("No Solution!\n");
			return 0;
		}
	}

	int tank = n,ans = 0;
	for(int i = 1;i <= k + 1;i++){
       // printf("tank = %d\n",tank);
		if(tank < A[i]){
			tank = n;
			ans++;
			//printf("Add fuel on %d\n",i - 1);
		}

		tank -= A[i];
	}

	printf("%d\n",ans);

	return 0;
}
