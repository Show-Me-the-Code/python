//#include "stdafx.h"
#include <iostream>
#include <deque>
#include <stack>
#include <algorithm>
using namespace std;
struct Node {
	int weight, order,code;	//weight表示权重，order表示输入顺序，code表示哈弗曼码
	char c;
	Node *LChild, *RChild;
}PNode[65], *ptr;

stack<Node*>Forest;

bool cmp(struct Node x, struct Node y) {
	return x.weight > y.weight;
}
int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		for (int j = 0; j < N; j++) {
			//PNode = new Node;
			cin >> PNode[j].c >> PNode[j].weight;
			PNode[j].order = j;
			PNode[j].LChild = PNode[j].RChild = NULL;
		}
		sort(PNode, PNode + N, cmp);
		/*
		for(int j=0;j<N;j++)
            cout<<PNode[j].c<<' '<<PNode[j].weight<<endl;
            */
        for(int j = 0; j < N; j++) {
            Forest.push(&PNode[j]);
           // cout << PNode[j] << endl;
        }
		for (int j = 0; j < N - 1; j++) {
			//cout << PNode;
			sort(PNode, PNode + N, cmp);
			ptr = new Node;
			cout << Forest.top() << endl;
			if (PNode[0].weight < PNode[1].weight) {
				ptr->LChild = &PNode[0];
				ptr->RChild = &PNode[1];

			}
			else {
				ptr->LChild = &PNode[1];
				ptr->RChild = &PNode[0];
			}
			cout << ptr->LChild << ' ' << ptr->RChild << endl;
			Forest.pop();
			//cout << Forest.top() << endl;
			Forest.pop();
			//cout << Forest.top() << endl;
			Forest.push(ptr);
		}
	}
}

