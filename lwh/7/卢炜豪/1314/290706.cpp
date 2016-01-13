#include <cstdio>
#define maxn 100000+2
int a[maxn];
void merge(int v,int u);
int getf(int v);
int main()
{
    int n,m,x,y;
    while(scanf("%d",&n)!=EOF)
    {

    for(int i=0;i<n;i++)
        a[i]=i;
    scanf("%d",&m);
    for(int i=0;i<m;i++)
    {
        scanf("%d %d",&x,&y);
        merge(x,y);
    }
    for(int i=0;i<n;i++)
        printf("a[%d]=%d\n",i,a[i]);
    int QA;
    scanf("%d",&QA);
    for(int i=0;i<QA;i++)
    {
        int j,k;
        scanf("%d %d",&j,&k);
        if(a[j]==a[k])
            printf("y\n");
        else
            printf("n\n");
    }

    }
    return 0;
}
void merge(int v,int u)
{
    int t1,t2;
    t1=getf(v);
    t2=getf(u);
    if(t1!=t2)
    {
        a[t2]=t1;
        //靠右原则，把右边的集合作为左边的左集合
        //经过路径压缩后，将a[u]的根的值也赋值为v的祖先a[t1];
    }
}
int getf(int v)
{
    if(a[v]==v)
        return v;
    else
    {
        //这里是路径压缩，每次在函数返回的时候，顺带把路上遇到的元素改到祖宗的集合下
        a[v]=getf(a[v]);
        return a[v];
    }
}
