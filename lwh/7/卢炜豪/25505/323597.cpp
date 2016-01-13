#include <cstdio>
#include <cstring>
long long loc[100000+5];
bool book[100000+5];
int main()
{
	long long N,T,ans = 0,Max;
	memset(book,false,sizeof(book));
	scanf("%lld %lld",&N,&T);
	//printf("%d %d\n",book[5],book[100]);
	for(int i=0 ; i<N ; i++) {
		long long l,s;
		scanf("%lld %lld",&l,&s);
		loc[i] = l + s * T;
	}

	Max = loc[0] ; book[0] = true;

	for(int i=1 ; i<N ; i++) {
		if(book[i]) continue;

		for(int j=i ; j<N ; j++) {

			if(loc[j] > Max) {
                //if(book[])
				book[j] = true;
				Max = loc[j];
			}
		}
		ans++;
		Max = 0;
	}
	printf("%lld\n",ans);
}
