#include <cstdio>

#define Max_ 200000 + 5
int find_num,book;
int find(int *data , int left , int right)
{
	if(left == right){
		if(find_num == data[left])
			book = left;
			//return;
	}
	else{

		int center = (left + right) / 2;

		find(data,left,center);
		find(data,center+1,right);
	}
	return book;
}
int main()
{
	int n;

	scanf("%d",&n);

		int data[Max_];

		for(int i = 0;i < n;i++)
			scanf("%d",&data[i]);

		int Num_find;
		scanf("%d",&Num_find);

		for(int i = 0;i < Num_find;i++){

            book = -1;
			scanf("%d",&find_num);

			//printf("%d\n",find(data,0,n-1));
			if(find(data,0,n-1) != -1){
                printf("%d\n",find(data,0,n-1));
			}
			else
                printf("Not Found\n");
		}
	return 0;
}
