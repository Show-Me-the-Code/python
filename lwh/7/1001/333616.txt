#include<stdio.h>
int main()
{
	printf("Hello World!\n");
	return 0;
}
/*
题号：1300
修改时间：2015-4-26
问题：INIT模块为完成
#include "stdafx.h"
#include <iostream>
#include <string>
using std::cout;
using std::cin;
using std::endl;
using std::string;
int len = 0;
typedef struct Node {
	int val;
	struct Node *next;
}Node,*PNode;

void insert(int val, int left,PNode *N) {
	//cout << "left = " << left << " len = " << len << endl;
	if (left > len) {
		if ((*N) == NULL) {
			(*N) = new Node;
			(*N)->val = val;
			(*N)->next = NULL;
			return;
		}
		else {
			insert(val, left, (&(*N)->next));
			return;
		}
	}
	if (left == 1) {
		PNode temp = new Node;
		if (*N != NULL) {
			temp = *N;
			*N = new Node;
			(*N)->val = val;
			(*N)->next = temp;
		}
		else if (*N == NULL) {
			*N = new Node;
			(*N)->val = val;
			(*N)->next = NULL;
		}
	}
	else
		insert(val, --left, (&(*N)->next));
	return;
}

bool Delete(int left, PNode *N) {
	//cout << "len = " << len-1 << endl;
	if (left > len)
		return false;
	if (left == 1) {
		PNode temp = new Node;
		temp = *N;
		*N = (*N)->next;
		delete temp;
		return true;
	}
	if (len == 1) {
		*N = NULL;
		return true;
	}
	else if (len >= 2) {
		if (left == 2) {
			PNode temp = new Node;
			temp = (*N)->next;
			(*N)->next = (*N)->next->next;
			delete temp;
			return true;
		}
		else if (left > 2) {
			Delete(--left, &(*N)->next);
		}
	}
	return true;
}

void init(PNode N) {
	N->next = NULL;
	//N = NULL;
	free(N);
}

void print(PNode N) {
	cout << N << endl;
	if (N != NULL) {
		cout << N->val << ' ';
		print(N->next);
	}
	return;
}

int main()
{
	int num_command;
	cin >> num_command;
	PNode root = new Node;
	//PNode NODE;
	root = NULL;
	while (num_command--) {
		string command;
		cin >> command;
		
		if (command == "INIT") {
			init(root);
		}
		else if (command == "PRINT") {
			print(root);
			cout << endl;
		}
		else if (command == "ADD") {
			len++;
			int address, value;
			cin >> address >> value;
			insert(value, address, &root);
		}
		else if (command == "LENGTH")
			cout << len << endl;
		else if (command == "DELETE") {
			int left;
			cin >> left;
			//cout << (*Find(value, &root))->val << endl;
			if (Delete(left, &root))
				len--;
			
		}
	}
}*/