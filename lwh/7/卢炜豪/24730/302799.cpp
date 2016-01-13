#include <cstdio>
int main()
{
   int N;
   while(scanf("%d",&N)!=EOF)
   {
       int count=0;
        if(N<=3)
            count=1;
        if(N==4)
            count=2;
        if(N>4)
        {
            while(N>2)
            {
                N/=3;
                count++;
                if(N<=5)
                    break;
              //  printf("count=%d\n",count);
            }
            if(N==5)
                count+=2;
            else
                count++;

        }
        printf("%d\n",count);
   }
}
