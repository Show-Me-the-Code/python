#include <cstdio>
#include <algorithm>
using namespace std;
int N,H;
struct Cow
{
    int w; int s;
    int h; int k;
}cow[25];
bool cmp(struct Cow a,struct Cow b)
{
    if(a.k-b.k>0)
        return true;
    else
        return false;
}
int A(int be,int en)
{
   // printf("be=%d en=%d ",be,en);
    int temp=cow[be-1].s-cow[be].w,res,sum_w=cow[be].w,g;
    for(int i=be-1;i>=en;i--){
        g=cow[i].s-sum_w;
        sum_w+=cow[i].w;
        if(g>temp)
            g=temp;
    }
    //printf("g=%d\n",g);
    return g;
}
int main()
{
    //int N,H;
    scanf("%d %d",&N,&H);
    for(int i=0 ; i<N ; i++){
        scanf("%d %d %d",&cow[i].h,&cow[i].w,&cow[i].s);
        cow[i].k=cow[i].s+cow[i].w;
    }
    sort(cow,cow+N,cmp);/*
    for(int i=0;i<N;i++){
        printf("%d\n",cow[i].k);
    }*/
    int L=0,be,en,ans=-1,temp;
    for(int i=N-1 ; i>=0 ; i--){
            L=cow[i].h;
        for(int j=i-1; j>=0 ; j--){
            L+=cow[j].h;
            if(L>=H){
                be=i,en=j;
                temp=A(be,en);
               // printf("temp=%d\n",temp);
                break;
            }
        }
        if(ans<temp)
            ans=temp;
    }
    printf("%d\n",ans);
}
