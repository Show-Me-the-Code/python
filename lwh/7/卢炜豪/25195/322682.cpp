#include <cstdio>
#include <cstring>
#define range 1000+1
struct info
{
	int speed;
	int time;
}cow1[range],cow2[range];

int main()
{
	int n,m,ans=0;
	memset(cow1,0,sizeof(cow1));
	memset(cow2,0,sizeof(cow2));
	scanf("%d %d",&n,&m);
	int t,time_sum=0,LenTime=0;
	for(int i=1;i<=n;i++)
    {
        scanf("%d %d",&cow1[i].speed,&t);
        time_sum+=t;
        LenTime+=t;
        cow1[i].time=time_sum;

    }
    time_sum=0;
    for(int i=1;i<=m;i++)
    {
        scanf("%d %d",&cow2[i].speed,&t);
        time_sum+=t;
        cow2[i].time=time_sum;
    }
//	int LenTime = 0;
	int j=1,k=1,loc1=0,loc2=0;
	int leader=0;
	int temp;

	for(int i = 1;i <= LenTime;i++)
	{
		if(i<=cow1[j].time)
		{
			loc1+=cow1[j].speed;
			if(i==cow1[j].time)
				j++;
		}
		if(i<=cow2[k].time)
		{
			loc2+=cow2[k].speed;
			if(i==cow2[k].time)
				k++;
		}
        //printf("loc1=%d j=%d loc2=%d k=%d\n",loc1,j,loc2,k);
        if(loc1!=loc2)
        {
            if(loc1>loc2)
                temp=1;
            else
                temp=2;
        }
        if(leader!=temp)
        {
            ans++;
            leader=temp;
        }


	}
	printf("%d\n",ans-1);
	return 0;
}
