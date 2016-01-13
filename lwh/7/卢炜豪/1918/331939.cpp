//#include "stdafx.h"
#include <iostream>
#include <deque>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;
struct Node {
	int weight, order, code;	//weight表示权重，order表示输入顺序，code表示哈弗曼码
	char c;
	Node *LChild, *RChild;
}PNode[65], *ptr, *tmp;

list<Node*>Forest;

bool cmp(struct Node x, struct Node y) {
	return x.weight < y.weight;
}
int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		for (int j = 0; j<N; j++) {
			PNode[j].weight = 0;
		}
		for (int j = 0; j < N; j++) {
			//PNode = new Node;
			cin >> PNode[j].c >> PNode[j].weight;
			PNode[j].order = j;
			PNode[j].LChild = PNode[j].RChild = NULL;
		}
		sort(PNode, PNode + N, cmp);
		///*
		//for(int j=0;j<N;j++)
		//cout<<PNode[j].c<<' '<<PNode[j].weight<<endl;
		//*/
		for (int j = 0; j < N; j++) {
			Forest.push_back(&PNode[j]);
			// cout << Forest.back() << endl;
		}
		tmp = new Node;
		tmp = Forest.front();
		ptr = new Node;

		for (int j = 0; j < N - 1; j++) {
			if (j == 0) {
				ptr->LChild = Forest.front();
				Forest.pop_front();
				ptr->RChild = Forest.front();
				Forest.pop_front();
				Forest.push_front(ptr);
			}
			else {
				ptr->LChild = tmp;
				ptr->RChild = Forest.front();
				Forest.pop_front();
				Forest.push_front(ptr);
			}
			tmp = new Node;
			if (!Forest.empty())
				tmp = Forest.front();
			//Forest.pop();
			ptr = new Node;
		}
		//cout << (Forest.front())->c << endl;
		for (list<Node*>::iterator i = Forest.begin(); i != Forest.end(); ++i) {
			cout << (*i)->weight << ' ' << (*i)->c << endl;
		}

	}
	//system("PAUSE");
}

