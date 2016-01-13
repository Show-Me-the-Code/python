/* ZQU OJ 1377 二叉查找树 
	插入、查找（包含找最小数）、删除、遍历四大模块
*/
//#include "stdafx.h"
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
}SerachTree, *PNode;    //记住结构体这种typedef用法

/*INSER函数这里，因为需要以一个节点的地址作为实参，所以这里是没必要把Root作为全局变量来使用的*/
void INSERT(key_type insert_num, PNode *root) {     //用二级指针作为函数参数，用来修改从主函数传过来的Root指针指向的地址。
	//初始化一个临时节点
	PNode tmp = (PNode)malloc(sizeof(SerachTree));
	tmp->key = insert_num;
	tmp->LChild = tmp->RChild = NULL;       //tmp的作用是临时节点
	//当为空树时
	if ((*root) == NULL) {      //root是Root的地址，*root = x 用来修改Root的指向    //当然用Root也行，但是这里是通过函数传递的形式来完成的
		*root = tmp;
		return;
	}
	//树非空
	//root是二级指针，没有被分配一个SerachTree单位，所用*root指向Root,&（*root)->x 传入地址
	else {
		if (insert_num < (*root)->key)   //递归，以左儿子做新的根节点
			INSERT(insert_num, &(*root)->LChild);	
		if (insert_num >(*root)->key)  //递归，以右儿子做新的根节点
			INSERT(insert_num, &(*root)->RChild);
	}
	return;
}

PNode FIND(key_type find_num, PNode point) {		//这里没有涉及到对数据的修改，不需要二级指针
	//PNode res = NULL;
	//cout << "point:" << endl;
	// cout << point->key << ' ' << (point->LChild) << ' ' << point->RChild <<endl;
	//point = (PNode)malloc(sizeof(SerachTree));   //不能再分配内存（传入一个地址，这个地址指向已有的结构体，不需要开新内存）
	//cout << "@" << endl;
	/*
		这里要注意不能cout出空指针指向的单元，不然会引发segmentation fault，切记。
		可以cout空指针的地址，但不能cout"空指针指向的内容“。
	*/
	if (point == NULL)		//节点为空时，返回一个NULL。这里作为递归基
		return NULL;
	if (find_num == point->key) {			
		//cout << "point->key=" << point->key << " point->LChild=" << point->LChild << " point->RChild=" << point->RChild <<endl;
		return point;		//如果找到了相等的元素，就返回这个节点的地址
	}
	else {
		//往左边走
		if (find_num < point->key /*&& point->LChild != NULL*/)
			FIND(find_num, point->LChild);
		//往右边走
		else if (find_num > point->key /*&& point->RChild != NULL*/)
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
	PNode Root;     //创建根节点，此时为空
	Root = (SerachTree*)malloc(sizeof(SerachTree));     //为其分配内存，这一步必须要！
	Root = NULL;        //将根节点指向空，这一步必须要！
	//Root->LChild = Root->RChild = NULL;       这一步不能下，Root此时为空，不存在LChild和RChild，使用会引起段错误
	while (cin >> command) {
		//getchar();
		if (command != "traverse") {
			//cout << '!';
			cin >> command_num;
			//cout << command << endl;
			if (command == "insert")
				INSERT(command_num, &Root);     //调用插入函数
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
