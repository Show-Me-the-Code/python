#include <iostream>
#include <algorithm>
using namespace std;
int ans = 0,T;
bool book[30];
struct R {
    int num;
    bool op;
}N[30];
void DFS(int END)
{
    //cout << END << endl;
    if(END == 1) {
        int sum = 0;
        for(int k=1; k<=T-1; k++) {
            if(N[k].op == true) {
                sum += N[k].num;
            }
            else if(N[k].op == false) {
                sum -= N[k].num;
            }
        }
        if(sum == T)
            ans++;
        //cout << "b" << endl;
        return;
    }
    for(int i=1; i<T; i++) {
        for(int j=1; j<=2; j++) {
            if(j==1)
                N[i].op = true;
            else
                N[i].op = false;
            //cout << "a" << endl;
            DFS(END-1);
        }
    }
    return;
}
int main()
{
    cin >> T;
    //cout << T;
    for(int i=1; i<T; i++) {
        N[i].num = i;
        book[i] = true;
    }
    DFS(T);
    cout<<ans<<endl;

}
