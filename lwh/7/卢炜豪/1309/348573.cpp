// OJ.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <stack>
#include <cstring>
using namespace std;

bool is_match(char x, char y) {
	int a1 = x;
	int a2 = y - 1;
	int a3 = y + 1;
	int b1 = x;
	int b2 = y + 2;
	int b3 = y - 2;
	if (a1 == a2 || a1 == a3 || b1 == b2 || b1 == b3) {
		return true;
	}
	else {
		return false;
	}
}
int main()
{
	char data[10000 + 2];
	while (cin >> data) {
		stack<char> sta;
		int length = strlen(data);
		for (int i = 0; i < length; i++) {
			if (sta.empty()) {
				sta.push(data[i]);
			}
			else {
				char temp = sta.top();
				sta.push(data[i]);
				if (is_match(temp, sta.top())) {
					sta.pop();
					sta.pop();
				}
			}
		}
		if (sta.empty()) {
			cout << "YES" << endl;
		}
		else {
			cout << "NO" << endl;
		}
	}
}
