#include <cstdio>

#define max_n 10000+5
int main()
{
	int M[max_n];

	int n;
	while(scanf("%d",&n)!=EOF){

		for(int i = 0;i < n;i++){
			scanf("%d",&M[i]);
		}
		int sum_max = 0;
		for(int i = 0;i < n;i++){

            int temp = 0;
			for(int j = i;j < n;j++){
                temp += M[j];

                if(temp > sum_max)
                sum_max = temp;
			}
		}

		printf("%d\n",sum_max);
	}
}
