#include <iostream>
#include <cmath>
#include <cstdio>
#define max 200000 + 5
using namespace std;

int find_num,book,data[max],center;
int Found(int left,int right)
{

	if(find_num == data[center] ){
		book = center;
	}
	if(fabs(left - right) == 1){
        if(find_num == data[left])
            book = left;
        if(find_num == data[right])
            book = right;
        return book;
	}
	else if(find_num < data[center]){
		right = center - 1;
		center = (left + right) / 2;
		Found (left , right);
	}
	else if(find_num > data[center]){
		left = center + 1;
		center = (left + right) / 2;
		Found(left,right);
	}

	return book;
}

int main()
{
    std::cout.sync_with_stdio(false);
	int n;
	cin>>n;
	for(int i = 1;i <= n;i++)
		cin>>data[i];
	int num;
	cin>>num;
	for(int i = 0;i < num;i++){
        book = -1;
		cin>>find_num;
		center = n/2;
		if(Found(1,n) != -1 ){
			cout<<Found(1,n) - 1<<endl;
        }
		else
			cout<<"Not Found"<<endl;
	}
}
