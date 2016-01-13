#include <cstdio>
struct mm
{
    int start,end;
};
int main()
{
    int N;
    struct mm s[100000+3];
    while(scanf("%d",&N)&&N)
    {
        for(int i=0;i<N;i++)
        {
            scanf("%d %d",&s[i].start,&s[i].end);
        }
        for(int i=1;i<N;i++)
            for(int j=0;j<N-i;j++)
        {
            if(s[j].end>s[j+1].end)
            {
                int temp=s[j].end;
                s[j].end=s[j+1].end;
                s[j+1].end=temp;

                int temp1=s[j].start;
                s[j].start=s[j+1].start;
                s[j+1].start=temp1;
            }
        }

  //      for(int i=0;i<N;i++)
   //         printf("%d %d\n",s[i].start,s[i].end);

        int sum=0,end1=0;
        for(int i=0;i<N;i++)
        {
            if(s[i].start>=end1)
            {
                sum++;
                end1=s[i].end;
            }
        }
        printf("%d\n",sum);
    }
}
