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
	int a3 = y - 2;
	if (a1==a2 || a1 == a3) {
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
		//cout << "length==" << length << endl;
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
		//cout << endl;
		if (sta.empty()) {
			cout << "YES" << endl;
		}
		else {
			cout << "NO" << endl;
		}
	}
}
