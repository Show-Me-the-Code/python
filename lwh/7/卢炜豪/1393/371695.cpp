
//#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#define Max 105
using namespace std;
typedef struct srt_node {
	int vertex;		//顶点值
	int weight;		//权值
	int out_degree = 0;		//入度
	int in_degree = 0;		//出度
}Node;
int main()
{
	int vertxt_num = 0,edge_num = 0;
	while (cin >> vertxt_num >> edge_num) {
		Node node[Max];//定义一个图
		int left_vertext=0, right_vertext=0;
		for (int i = 0; i < edge_num; i++) {
			cin >> left_vertext >> right_vertext;
			node[left_vertext].out_degree++;
			node[right_vertext].in_degree++;
		}
		int flag = 0;
		for (int i = 1; i <= vertxt_num; i++) {
			//printf("node[%d].indegree=%d\n", i,node[i].in_degree);
			if (node[i].in_degree == 0) {
				flag = 1;
			}
		}
		if (edge_num == 0)
			flag = 1;
		if (flag == 1) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
}