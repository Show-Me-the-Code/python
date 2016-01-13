//#include "stdafx.h"
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
		if ((*N) == nullptr) {
			(*N) = new Node;
			(*N)->val = val;
			(*N)->next = nullptr;
			return;
		}
		else {
			insert(val, left, (&(*N)->next));
			return;
		}
	}
	if (left == 1) {
		PNode temp = new Node;
		if (*N != nullptr) {
			temp = *N;
			*N = new Node;
			(*N)->val = val;
			(*N)->next = temp;
		}
		else if (*N == nullptr) {
			*N = new Node;
			(*N)->val = val;
			(*N)->next = nullptr;
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
		*N = nullptr;
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
	if (N != nullptr) {
		PNode temp = new Node;
		temp = N;
		N = N->next;
		delete temp;
		init(N);
	}
}

void print(PNode N) {
	while (N != nullptr) {
		cout << N->val << ' ';
		N = N->next;
	}
	cout << endl;
	return;
}

int main()
{
	int num_command;
	cin >> num_command;
	PNode root = new Node;
	//PNode NODE;
	root = nullptr;
	while (num_command--) {
		string command;
		cin >> command;
		
		if (command == "INIT") {
			init(root);
		}
		else if (command == "PRINT") {
			print(root);
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
}