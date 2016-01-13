#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<long long int> cow;
int main()
{
	long long int N,T;
	scanf("%lld %lld",&N,&T);
	long long int loc,speed;
	for(int i=0 ; i<N ; i++){
		scanf("%lld %lld",&loc,&speed);
		long long int tra = loc + speed * T;
		loc = - tra;
		if(cow.empty()==1 || loc >= cow.back()){
			cow.push_back(loc);
		}
		else{
            *upper_bound(cow.begin(),cow.end(),loc) = loc;
		}
	}
	//printf("!\n");
	cout<<cow.size()<<endl;
	return 0;
}
