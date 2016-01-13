/* ZQU OJ 1377 二叉查找树 */
#include "stdafx.h"
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <stack>
bool FLAG = false;
using namespace std;
typedef int key_type;
typedef struct SerachTree {
	key_type key;
	struct SerachTree *LChild, *RChild;
}SerachTree, *PNode;	//记住结构体这种typedef用法

void INSERT(key_type insert_num, PNode root) {		//用二级指针作为函数参数，用来修改一级指针指向的地址。因为
	//初始化一个临时节点
	PNode tmp = (PNode)malloc(sizeof(SerachTree));
	tmp->key = insert_num;
	tmp->LChild = tmp->RChild = NULL;
	//当为空树时
	if (root == NULL) {
		root = tmp;
		return;
	}
	//树非空
	else {
		if (insert_num < root->key)   //递归，以左儿子做新的根节点
			INSERT(insert_num,root->LChild);
		if (insert_num > root->key)  //递归，以右儿子做新的根节点
			INSERT(insert_num,root->RChild);
	}
	return;
}
PNode FIND(key_type find_num, PNode point) {
	//PNode res = NULL;
	//cout << "point:" << endl;
	// cout << point->key << ' ' << (point->LChild) << ' ' << point->RChild <<endl;
	//point = (PNode)malloc(sizeof(SerachTree));   //不能再分配内存（传入一个地址，这个地址指向已有的结构体，不需要开新内存）
	//cout << "@" << endl;
	if (point == NULL)
		return NULL;
	if (find_num == point->key) {
		//cout << "point->key=" << point->key << " point->LChild=" << point->LChild << " point->RChild=" << point->RChild <<endl;
		return point;
	}
	else {
		//往左边走
		if (find_num < point->key && point->LChild != NULL)
			FIND(find_num, point->LChild);
		else if (find_num > point->key && point->RChild != NULL)
			FIND(find_num, point->RChild);
		else return NULL;
	}

	//return res;
}
//遍历二叉树，中序
void TRAVERSE(PNode N) {
	//如果该树为空
	//cout << "N->key=" << N->key <<endl;
	//N = (PNode)malloc(sizeof(SerachTree) );
	// cout << N->LChild << ' ' << N->RChild << endl;
	//FLAG = false;
	if (N != NULL) {
		//if(N->LChild != NULL)
		FLAG = true;
		TRAVERSE(N->LChild);
		// else return;
		cout << N->key << ' ';
		//if(N->RChild != NULL)
		TRAVERSE(N->RChild);
		//else return;
	}
	else return;
}
PNode FindMin(PNode T) {
	if (T == NULL)
		return NULL;
	if (T->LChild == NULL)
		return T;
	else
		FindMin(T->LChild);
}
void DELETE(key_type delete_num, PNode *N) {
	PNode TmpCell;
	TmpCell = (PNode)malloc(sizeof(SerachTree));
	//空树
	if ((*N) == NULL)
		return;
	else if (delete_num < (*N)->key) {
		DELETE(delete_num, &(*N)->LChild);
	}
	else if (delete_num >(*N)->key) {
		DELETE(delete_num, &(*N)->RChild);
	}
	//两个儿子
	else if ((*N)->LChild && (*N)->RChild) {
		TmpCell = FindMin((*N)->RChild);
		(*N)->key = TmpCell->key;
		DELETE((*N)->key, &(*N)->RChild);
	}
	//一个儿子||叶节点
	else {
		TmpCell = *N;
		if ((*N)->LChild == NULL/* && (*N)->RChild != NULL*/)
			*N = (*N)->RChild;
		else if ((*N)->RChild == NULL/* && (*N)->LChild != NULL*/)
			(*N) = (*N)->LChild;
		//cout << TmpCell->key << ' ' << TmpCell->LChild << ' ' << TmpCell->RChild << endl;
		//删除节点
		//cout << "N =" << N << endl;
		free(TmpCell);
		//(*N )= NULL;
		TmpCell = NULL;
		//*N = NULL;
		//N = NULL;
		//cout << TmpCell->key << ' ' << TmpCell->LChild << ' ' << TmpCell->RChild << endl;
		//cout << (*N)->key << ' ' << (*N)->LChild << ' ' << (*N)->RChild << endl;
		return;
	}

}
int main()
{
	string command;
	int command_num;
	PNode Root;		//创建根节点，此时为空
	Root = (SerachTree*)malloc(sizeof(SerachTree));		//为其分配内存，这一步必须要！
	Root = NULL;		//将根节点指向空，这一步必须要！
	//Root->LChild = Root->RChild = NULL;		这一步不能下，Root此时为空，不存在LChild和RChild，使用会引起段错误
	while (cin >> command) {
		//getchar();
		if (command != "traverse") {
			//cout << '!';
			cin >> command_num;
			//cout << command << endl;
			if (command == "insert")
				INSERT(command_num, Root);		//调用插入函数
			//cout <<Root;
			if (command == "find") {
				string find_res[2] = { "yes", "no" };
				if (FIND(command_num, Root) != NULL) {
					cout << find_res[0] << endl;
				}
				else cout << find_res[1] << endl;
			}
			if (command == "delete") {
				DELETE(command_num, &Root);
			}
		}
		else if (command == "traverse") {
			//cout << command <<endl;
			FLAG = false;
			TRAVERSE(Root);
			if (FLAG)
				cout << endl;
		}
	}
}
