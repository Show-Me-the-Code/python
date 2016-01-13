#include <cstdio>
#include <cstring>
int day[2][13]={{0,31,28,31,30,31,30,31,31,30,31,30,31},{0,31,29,31,30,31,30,31,31,30,31,30,31}};
int leap(int k);
int main()
{
    int N;
    while(scanf("%d",&N)!=EOF)
    {
        int year=1900;
        int out=1900+N;
        int sun_sat[8];
        memset(sun_sat,0,sizeof(sun_sat));
        int it=13;
        while(year<out)
        {
            int q=7;
            if(leap(year)==1)//是闰年的情况
            {//   printf("1\n");
                for(int i=1;i<=12;i++)
                    {
                        int w=it%7;
                        if(w==0)
                        w=7;
                        sun_sat[w]++;
                    //    printf("!=%d\n",w);
                        it=it+day[1][i];
                //        printf("it=%d\n",it);
                    }
            }
            if(leap(year)==0)
            {
              //  printf("0\n");
                for(int i=1;i<=12;i++)
                {
                    int w=it%7;
                    if(w==0)
                    w=7;
                    sun_sat[w]++;
               //     printf("!=%d\n",w);
                    it=it+day[0][i];
                  //  printf("it=%d\n",it);
                }
            }


            year++;
        //    printf("out=%d year=%d N=%d\n",out,year,N);
         }
         printf("%d %d ",sun_sat[6],sun_sat[7]);
         for(int i=1;i<=5;i++)
            printf("%d ",sun_sat[i]);
            printf("\n");

    }

    return 0;
}

int leap(int k)
{
    if(k%4==0&&k%100!=0)
        return 1;
    else if(k%400==0)
        return 1;

    return 0;
}
