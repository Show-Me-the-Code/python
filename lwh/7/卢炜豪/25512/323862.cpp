#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
const int Maxn = 500000+5;
using namespace std;

struct Cow {
    long long int  loc;
    string info,left;
}cow[Maxn];

int cmp(struct Cow a,struct Cow b) {
    return a.loc < b.loc;
}

int main()
{
    long long int N,A,B;
    cin>>N>>A>>B;
    long long int ANS = B-A+1;
    long long int NS_num = 0; //记录NS的点数 ，最后再减去
    for(int i=0; i < N; i++) {
        cin>>cow[i].info>>cow[i].loc;
        if(cow[i].info == "NS")
            NS_num++;
    }
   // cout<<endl;
    sort(cow,cow+N,cmp);

    for(int i=1; i<N; i++) {  //构建左边的信息
        cow[i].left = cow[i-1].info;
    }
    //单独判断两个端点
    int tmp = 0;//tmp表示要减去的点数
   // for(int i=0; i<N; i++) cout<<cow[i].loc<<' '<<cow[i].info<<endl;
    //cout<<endl;
    if(cow[0].loc != A && cow[0].info == "NS") {
        tmp += cow[0].loc - A;
      //  cout<<"tmp1="<<tmp<<endl;
    }
    if(cow[N-1].loc!= B && cow[N-1].info == "NS") {
        tmp += B - cow[N-1].loc ;
       // cout<<"tmp2="<<tmp<<endl;
    }

    for(int i = 1; i < N; i++) {
		if(cow[i].info == "NS" && cow[i].left == "S") {
			tmp += (cow[i].loc - cow[i-1].loc - 1) / 2;
			//cout<<"tmp3="<<tmp<<endl;
		}
		else if(cow[i].info == "NS" && cow[i].left == "NS") {
			tmp += cow[i].loc - cow[i-1].loc - 1;
			//cout<<"tmp4="<<tmp<<endl;
		}
		else if(cow[i].info == "S" && cow[i].left == "NS") {
			tmp += (cow[i].loc - cow[i-1].loc - 1) / 2;
			//cout<<"tmp5="<<tmp<<endl;
		}
	}

	//cout<<"ANS="<<ANS<<' '<<"tmp="<<tmp<<' '<<"NS_num="<<NS_num<<endl;
	cout<<ANS-tmp-NS_num<<endl;

	return 0;

}
