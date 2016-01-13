#include <cstdio>
#include <algorithm>

#define Max_ 10+2

using namespace std;

int main()
{
	int N,K;

	while(scanf("%d %d",&N,&K) != EOF){

		int A[Max_];

		if(N == 0 && K == 0)
			return 0;

		int sum_left = 1, sum_right = 1, sum_cross = 1;

		for(int i = 0;i < N; i++){
			scanf("%d",&A[i]);
		}

		sort(A,A+N);

		for(int i = 0; i < K ;i++){

			if(A[i] > 0)
				break;

			sum_left *= A[i];
		}

		for(int i = 0 , k = N -1;i < K;i++ , k--){

			if(A[k] < 0)
				break;

			sum_right *= A[k];
		}

		for(int k = 2;k < K ;k += 2){

            sum_cross = 1;
            
			for(int i = 0; i < k;i++){

                if(A[i] > 0)
                    break;

				sum_cross *= A[i];
			}

			for(int j = K - k,w = N -1;j > 0;j--,w--){

				if(A[w] < 0)
                    break;

				sum_cross *= A[w];
			}
		}

		int result = max(sum_cross,max(sum_left,sum_right));
		//printf("sum_left = %d sum_right = %d sum_corss = %d\n",sum_left,sum_right,sum_cross);
		printf("%d\n",result);

	}

	return 0;
}
