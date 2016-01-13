//#include "stdafx.h"
#include <iostream>
#include <deque>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
struct Node {
	int weight, order, code;	//weight表示权重，order表示输入顺序，code表示哈弗曼码
	char c;
	string HuffCode;
	Node *LChild, *RChild;
}PNode[65], *ptr, *tmp,PNode1[65];

//string HuffCode[65];
list<Node*>Forest;
vector<Node*>E;
map<string, char> P[65];

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
		char I[65];
		for (int j = 0; j < N; j++) {
			PNode[j].weight = 0;
			PNode[j].c = '-1';
		}
		for (int j = 0; j < N; j++) {
			//PNode = new Node;
			cin >> PNode[j].c >> PNode[j].weight;
			PNode[j].order = j;
			PNode[j].LChild = PNode[j].RChild = NULL;
			PNode1[j] = PNode[j];
		}
		sort(PNode, PNode + N, cmp);
		///*
		//for(int j=0;j<N;j++)
		//cout<<PNode[j].c<<' '<<PNode[j].weight<<endl;
		//*/
		for (int j = 0; j < N; j++) {
			Forest.push_back(&PNode[j]);
			//cout << Forest.back()->weight << endl;
		}
		tmp = new Node;
		tmp = Forest.front();
		ptr = new Node;
		ptr->weight = 0;
		//cout << "##" << Forest.front()->weight;
		for (int j = 0; j < N - 1; j++) {
			/*if (!E.empty())
			cout << "# " << E.back()->weight << endl;
			cout << "$ " << ptr->weight << endl;*/
			if (j == 0) {
				ptr->LChild = Forest.front();
				ptr->weight += Forest.front()->weight;
				//cout << "!" << Forest.front()->weight << endl;
				//cout << "#" << ptr->weight << endl;
				Forest.pop_front();
				ptr->RChild = Forest.front();
				ptr->weight += Forest.front()->weight;
				Forest.pop_front();
				E.push_back(ptr);
				//Forest.push_front(ptr);
				//cout << "@" << E.front()->weight << endl;
			}
			else {
				ptr->LChild = tmp;
				ptr->RChild = Forest.front();
				//cout << "* " << ptr->weight << endl;
				//cout << Forest.front() << ' ' << E
				ptr->weight = Forest.front()->weight + E.back()->weight;
				//cout << "** " << ptr->weight << endl;
				Forest.pop_front();
				//Forest.push_front(ptr);
				E.push_back(ptr);
			}
			tmp = new Node;
			int temp_w = 0;
			if (!E.empty()) {
				tmp = E.front();
			}
			if (!Forest.empty())
				temp_w = Forest.front()->weight;
			ptr = new Node;
			ptr->weight = temp_w;
		}
		//以上构造哈弗曼树完毕
		/*
		for (int j = N-2; j > 0; j--)
			cout << E[j]->RChild->c << ' ' << E[j]->RChild->weight << endl;
		cout << E[0]->LChild->c << ' ' << E[0]->LChild->weight << endl;
		cout << E[0]->RChild->c << ' ' << E[0]->RChild->weight << endl;
		*/
		
		for (int j = 0; j < N; j++) {
			cout << PNode1[j].c << ' ' << PNode1[j].weight << ' ';
			for (int k = N-2; k >=0; k--) {
				//cout << "PNode1[" << j << "].c==" << PNode1[j].c << ' ' << "E[" << k << "]->RChild->c==" << E[k]->RChild->c << endl;
				if (k != 0) {
					if (PNode1[j].c == E[k]->RChild->c) {
						cout << '1' << endl;
						break;
					}
					else
						cout << '0';
				}
				else {
					if (PNode1[j].c == E[k]->RChild->c) {
						cout << '1' << endl;
						break;
					}
					else {
						cout << '0' << endl;
						break;
					}
				}
			}
		}
		
		
	}
	system("PAUSE");
}

