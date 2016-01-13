//#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <stdlib.h>
using namespace std;

/*
	图用邻接表实现
	判断图是否存在合法的拓扑序列
*/
const int SIZE = 105;
int isEmpty = 0;
typedef struct NEXTNODE {
	int in_degree;
	int out_degree;
	int in;
	int num;
	struct NEXTNODE* next;
}NextNode;

struct HEADNODE {
	int in_degree;
	int out_degree;
	int next_num;
	int in;
	NextNode* next;
}HeadNode[SIZE];


void init() {
	//初始化结构体数组的数据,清0
	for (int i = 0; i < SIZE; i++) {
		HeadNode[i].in = 0;
		HeadNode[i].in_degree = 0;
		HeadNode[i].out_degree = 0;
		HeadNode[i].next = NULL;
	}
}
void OutInfo() {
	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1) {
			cout << i << " indegree:" << HeadNode[i].in_degree << " outdegree:" << HeadNode[i].out_degree;
			cout << endl;
		}
	}

	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1) {
			cout << i;
			for (NextNode* temp = HeadNode[i].next; temp != NULL; temp = temp->next) {
				cout << " ->" << temp->num;
			}
			cout << endl;
		}
	}
	cout << endl;
}
int FindZeroIndegree() {
	int ans_num = 0;
	int flag = 0;
	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1 && HeadNode[i].in_degree == 0) {
			//cout << "i="<<i <<"in_degree" << HeadNode[i].in_degree << endl;
			flag = 1;
			ans_num = i;
			break;
		}
		
	}	
	//return (ans_num = 0);
	if (flag == 0) {
		
		int flag1 = 0;
		for (int i = 0; i < SIZE; i++) {
			if (HeadNode[i].in == 1) {
				flag1 = 1;
                                break;
			}
		}
		if (flag1 == 0) {
			ans_num = -2;
		}
		else if (flag1 == 1) {
			ans_num = -1;
		}
	}
	else if (flag == 1) {
		//cout << "h" << return_num << endl;
		ans_num = ans_num;
	}
	return ans_num;
}


//剪边
void cutNode() {
	while (1) {
		int zeroIndex = FindZeroIndegree();
	//	cout << "zeroIndex=" << zeroIndex << endl;
		if (zeroIndex == -1) {
			cout << "NO" << endl;
			return;
		}
		else if (zeroIndex == -2) {
			cout << "YES" << endl;
			return;
		}
		//cout << "zeorIndex=" << zeroIndex << endl;
		HeadNode[zeroIndex].in = -1;
		NextNode* temp = HeadNode[zeroIndex].next;
		while (temp != NULL) {
			int index = temp->num;
			HeadNode[index].in_degree--;
			temp = temp->next;
		}
		//OutInfo();
	}
}
void foo(int n, int e) {
	//调用初始化函数
	init();
	int a, b;
	//此for循环用来构建图
	for (int i = 0; i < e; i++) {
		cin >> a >> b;
		HeadNode[a].in = 1;
		HeadNode[b].in = 1;
		//HeadNode[b].in_degree++;

		/*
			给头结点添加邻接点
			1.添加第一个邻接点 if
			2.添加非第一个邻接点 else
		*/
		if (HeadNode[a].next == NULL) {
			//cout << "run if" << endl;
			NextNode* next_node = (NextNode*)malloc(sizeof(NextNode));
			next_node->num = b;
			next_node->in = 1;
			next_node->next = NULL;
			next_node->in_degree=0;
			HeadNode[a].next = next_node;
			HeadNode[a].next_num = b;
		}
		else {
			//cout << "run else" << endl;
			NextNode* next_node = (NextNode*)malloc(sizeof(NextNode));
			next_node->num = b;
			next_node->next = NULL;
			next_node->in_degree=0;
			next_node->in = 1;
			NextNode* temp;
			temp = HeadNode[a].next;
			while (temp->next != NULL) {
				//cout << "else@" << temp->num << endl;
				temp = temp->next;
			}
			temp->next = next_node;
		}
	}

	//录取每个结点的出度入度信息
	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1) {
			NextNode* temp = HeadNode[i].next;
			while (temp != NULL) {
				int index = temp->num;
				HeadNode[index].in_degree++;
				HeadNode[i].out_degree++;
				temp = temp->next;
			}
		}
	}

	//OutInfo();

	cutNode();
	//cout << HeadNode[105].in << " " << HeadNode[105].in_degree << endl;
	return;

}
int main()
{
	//n表示顶点数,e表示边数
	int n, e;
	while (cin >> n >> e) {
		foo(n, e);

	}
}