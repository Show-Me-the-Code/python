#include <stdio.h>

int cutbinumber(int b[],int cutnum,int n);

int main()
{
    int b[1005],N;

    scanf("%d",&N);

    for(int i=0;i<N;i++)
        scanf("%d",&b[i]);

    int outputnum=0;
    for(int i=0;i<N;i++)
    {
        int reachnum=cutbinumber(b,b[i],N);

       // printf("reachnum=%d\n",reachnum);

        if(reachnum>outputnum)
            outputnum=reachnum;
    }

    printf("%d\n",outputnum);
}

int cutbinumber(int b[],int cutnum,int n)
{
    int comparenum,i=0,count=0,max=0,k=0;

    while(i<n)
    {
        if(b[i]!=cutnum)
        {
            comparenum=b[i];
            break;
        }
        i++;
    }
   // printf("%d\n",comparenum);

    for(int i=0;i<n;i++)
    {
        if(b[i]!=cutnum)
        {

            if(b[i]==comparenum)
           {
                count++;
               // printf("count=%d\n",count);
           }
            else if(b[i]!=comparenum)
               {
                    comparenum=b[i];
                    count=1;
               }
        }
       // printf("k=%d ",k);
        if(count>max)
            max=count;
    }

    return max;
}

