#include <cstdio>
#include <algorithm>
#include <cmath>
#define Max 100 + 5

struct Each_car
{
	int loc;		//汽车的坐标
	int speed;		//汽车的速度
	double rec_time;//和Anna的车相遇的时间
};

int main()
{
	int l,s,d,n,t = 1;
	while(scanf("%d %d %d %d",&l,&s,&d,&n) != EOF)
	{
		struct Each_car car[Max];
		double time = 0;double min_time = 99999999;
		int k = 0;  //time纪录总时间 car_i记录与Anna相遇车的代号(可能与多辆车相遇)

		if(l == 0 && s == 0 && n == 0 && d == 0)
			return 0;

		for(int i = 0;i < n;i++)
		{
			scanf("%d %d",&car[i].loc,&car[i].speed);	//输入每辆车的坐标和速度

			if(car[i].loc <= l && car[i].speed > s)
			{
				double temp_min = (l - car[i].loc) / (car[i].speed - s);
				if(temp_min < min_time)
					min_time = temp_min;
			}
			else if(car[i].loc > l && s > car[i].speed )
			{
				double temp_min = (car[i].loc - l) / (s - car[i].speed);
				if(temp_min < min_time)
					min_time = temp_min;
			}
		}

		//更新Anna的坐标信息
		l += s * min_time ;//printf("min_time=%lf l=%d\n",min_time,l);
		time += min_time;

		while(l < d)   //当Anna的车没到达终点
		{
			int temp_speed = 0,num_meet = 0;

			//更新相遇后其他所有车的位置信息
			for(int i = 0;i < n;i++)
			{
				car[i].loc += car[i].speed * min_time;

				if(car[i].loc == l)  //如果该车与Anna的车相遇（重合）
				{
					temp_speed += car[i].speed;
					num_meet++;
				}
			}

			//更新Anna的信息
			s = (s + temp_speed) / (num_meet + 1);
			l += s * (int)min_time ;

			time += min_time;

			//再找出Anna的车下一次与其他车相遇时的最短时间
			for(int i = 0;i < n;i++)
			{
				int speed_ = fabs(car[i].speed - s);
                double time_ = (double)speed_  / ((double)fabs(car[i].loc - l));
                //printf("speed_=%d abs(car[%d].loc - l)=%d time_=%lf\n",speed_,i,abs(car[i].loc-l),time_);

				if(car[i].loc <= l && car[i].speed > s)
				{
					double temp_min = (l - car[i].loc) / (car[i].speed - s);
					if(temp_min < min_time)
						min_time = temp_min;
				}
				else if(car[i].loc > l && s > car[i].speed )
				{
					double temp_min = (car[i].loc - l) / (s - car[i].speed);
					if(temp_min < min_time)
						min_time = temp_min;
				}
			}
			//printf("min_time = %lf ",min_time);

			//printf("l=%d\n",l);

		}
		printf("Case %d: Anna reaches her destination at time %lf at a speed of %d\n",t,time,s);
		t++;
		//printf("%lf %d\n",time,s);
	}

	return 0;
}
