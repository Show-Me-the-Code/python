#include <cstdio>
#include <algorithm>
using namespace std;
long long int N,H;
struct Cow
{
    long long int w;long long int s;
    long long int h;long long int k;
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
    //printf("be=%d en=%d ",be,en);
    int temp=cow[be-1].s-cow[be].w,res,sum_w=cow[be].w,g;
    for(int i=be-1;i>=en;i--){
        g=cow[i].s-sum_w;
        sum_w+=cow[i].w;
       // printf("g=%d\n",g);
        if(g>temp)
            g=temp;
    }
    //printf("g=%d\n",g);
    return g;
}
int main()
{
    //int N,H;
    scanf("%lld %lld",&N,&H);
    for(int i=0 ; i<N ; i++){
        scanf("%lld %lld %lld",&cow[i].h,&cow[i].w,&cow[i].s);
        cow[i].k=cow[i].s+cow[i].w;
    }
    sort(cow,cow+N,cmp);/*
    for(int i=0;i<N;i++){
        printf("%d\n",cow[i].k);
    }*/
    long long int L=0,be,en,ans=-1,temp;
    for(int i=N-1 ; i>=0 ; i--){
            L=cow[i].h;
        for(int j=i-1; j>=0 ; j--){
            L+=cow[j].h;
           // printf("L=%d\n",L);
            if(L>=H){
                be=i,en=j;
                temp=A(be,en);
                //printf("temp=%d\n",temp);
                break;
            }
        }
        if(ans<temp)
            ans=temp;
    }
    printf("%lld\n",ans);
}
