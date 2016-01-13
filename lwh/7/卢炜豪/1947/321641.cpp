#include <cstdio>
#define max_n 10000+5
using namespace std;

int Cal_MaxSum(int *A,int left,int right)
{
	int sum = 0;
//	int a[max_n];
	if(left == right)
	{
		sum = A[left]>0 ? A[left] : 0;
	//	printf("sum = %d\n",sum);
	}
	else
	{
		int center = (left+right)/2;
		//printf("center = %d\n",center);
		int leftsum = Cal_MaxSum(A,left,center);
		int rightsum = Cal_MaxSum(A,center+1,right);

		int s1 = 0;
		int lefts = 0;
		for(int i=center; i>=left;i--)
		{
		  //  printf("yo! center=%d left=%d right=%d\n",center,left,right);
			lefts += A[i];
			if(lefts>s1)
				s1=lefts;
		}

		int s2 = 0;
		int rights = 0;
		for(int i=center+1; i<=right;i++)
		{
			rights += A[i];
			if(rights>s2)
			{
				s2=rights;
			}
		}
		sum = s1+s2;
		if(sum<leftsum)
			sum = leftsum;
		if(sum<rightsum)
			sum = rightsum;
	}
	return sum;
}

int main()
{
    int n;
    while(scanf("%d",&n) != EOF){
        int A[max_n];

        for(int i = 0;i < n;i++)
            scanf("%d",&A[i]);

        printf("%d\n",Cal_MaxSum(A,0,n-1));
    }
	return 0;
}
