#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
struct move
{
	char name[200];
	int loc;
};
bool cmp(struct move a,struct move b)
{
	 if(strcmp(a.name,b.name) > 0)
        return false;
     return true;
}
int main()
{
	int n;
	while(scanf("%d",&n) != EOF)
	{
	    if(n == 0)
            return 0;
        struct move To[1002];

		for(int i = 0;i < n;i++)
		{
			cin>>To[i].name;
			To[i].loc = i;
		}

		sort(To,To + n,cmp);


        int step = 0;

        for(int i = 0;i < n; i++)
        {
            step += fabs(i - To[i].loc);
        }
        printf("%d\n",step);
	}
	return 0;
}
