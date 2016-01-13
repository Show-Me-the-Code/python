#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std;
struct info {
    int index;
    int x;
    int y;
}N[100];
bool cmp1(struct info a, struct info b) {
    if(a.x != b.x) {
        return a.x < b.x;
    }
    else
        return a.y < b.y;
}
/*
bool cmp2(struct info a,struct info b) {
    if(a.x == b.x) {
        return a.y < b.y;
    }
    else
        return;
}*/
int main()
{
    int n,i;
    scanf("%d",&n);
    for(i=0; i<n; i++) {
        scanf("%d %d %d",&N[i].index,&N[i].x,&N[i].y);
    }
    sort(N,N+i,cmp1);
    for(int j=0; j<i; j++) {
        printf("%d ",N[j].index);
    }
    //sort(N,N+i,cmp2);
}
