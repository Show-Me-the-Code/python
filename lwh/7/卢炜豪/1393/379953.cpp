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
		HeadNode[i].in = -1;
		HeadNode[i].in_degree = 0;
		HeadNode[i].out_degree = 0;
		HeadNode[i].next = NULL;
	}
}
void foo(int n,int e) {
	//调用初始化函数
	init();
	int a, b;
	//此for循环用来构建图
	for (int i = 0; i < e; i++) {
		cin >> a >> b;
		HeadNode[a].in = 1;
		HeadNode[b].in = 1;

		/*
			给头结点添加邻接点
			1.添加第一个邻接点 if
			2.添加非第一个邻接点 else
		*/
		if (HeadNode[a].next == NULL) {
			//cout << "run if" << endl;
			NextNode* next_node = (NextNode*)malloc(sizeof(NextNode));
			next_node->num = b;
			next_node->next = NULL;
			next_node->in_degree = 0;
			HeadNode[a].next = next_node;
			HeadNode[a].next_num = b;
		}
		else {
			//cout << "run else" << endl;
			NextNode* next_node = (NextNode*)malloc(sizeof(NextNode));
			next_node->num = b;
			next_node->next = NULL;
			next_node->in_degree = 0;

			NextNode* temp ;
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

	//检查每个结点的出入度信息
	//cout << "before:" << endl;
	/*
	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1) {
			cout << i << " indegree:" << HeadNode[i].in_degree << " outdegree:" << HeadNode[i].out_degree;
			cout << endl;
		}

	}*/
	

	//判断是否存在拓扑序列
	//1.剪边
	//2.扫描处理
	//cout << "after:" << endl;
	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1 && HeadNode[i].in_degree == 0) {
			HeadNode[i].in = -1;
			NextNode* temp = HeadNode[i].next;
			while (temp != NULL) {
				int index = temp->num;
				HeadNode[index].in_degree--;
				temp = temp->next;
			}
		}
	}
	/*
	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1) {
			cout << i << " indegree:" << HeadNode[i].in_degree << " outdegree:" << HeadNode[i].out_degree;
			cout << endl;
		}

	}*/
	int flag = 0;
	for (int i = 0; i < SIZE; i++) {
		if (HeadNode[i].in == 1) {
			flag = 1;
			break;
		}

	}
	if (flag == 0) {
		cout << "YES" << endl;
	}
	else if (flag == 1) {
		cout << "NO" << endl;
	}
	return;
	
}
int main()
{
	//n表示顶点数,e表示边数
	int n, e;
	while (cin >> n >> e) {
		foo(n, e);
		/*
		for (int i = 0; i < SIZE; i++) {
			if (HeadNode[i].in == 1) {
				cout << i;
				for (NextNode* temp = HeadNode[i].next;temp != NULL;temp = temp->next) {
					cout << " ->" << temp->num;
				}
				cout << endl;
			}
		}*/
	}
}