#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int cas;
    scanf("%d",&cas);
    while(cas--) {
        long long int Fprice;
        long long int P[100+5];
        scanf("%lld",&Fprice);
        int n;
        scanf("%d",&n);
        for(int i=0; i<n; i++) {
            scanf("%lld",&P[i]);
        }
        sort(P,P+n);
        long long int in = n-1;
        for(int i=0; i<n; i++) {
            if(P[i]<=Fprice && P[i+1]>Fprice)
                in = i;
        }
        long long int sum1 = 0,t1=0;
        for(int i=in; i>=0; i--) {
            sum1 += P[i];
            t1++;
            if(sum1>=Fprice) {
                break;
            }
        }
        long long int sum2 = 0,t2=0;
        for(int i=0; i<n; i++) {
            sum2 += P[i];
            t2++;
            if(sum2>=Fprice) {
                break;
            }
        }
        //printf("sum1=%lld t1=%lld sum2=%lld t2=%lld\n",sum1,t1,sum2,t2);
        int ans1 = min(sum1,sum2);
        if(ans1==sum1) {
            printf("%lld %lld\n",sum1,t1);
        }
        else if(ans1==sum2) {
            printf("%lld %lld\n",sum2,t2);
        }
    }
    return 0;
}
