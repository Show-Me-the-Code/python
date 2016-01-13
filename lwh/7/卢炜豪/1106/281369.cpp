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

        if(reachnum>outputnum)
            outputnum=reachnum;
    }

    printf("%d\n",outputnum);
}

int cutbinumber(int b[],int cutnum,int n)
{
    int comparenum,i=n,count=0,max=0;

    while(i--)
    {
        if(b[i]!=cutnum)
            comparenum=b[i];
    }

    for(int i=0;i<n;i++)
    {
        if(b[i]!=cutnum)
        {

            if(b[i]==comparenum)
                count++;

            else if(b[i]!=comparenum)
                comparenum=b[i];
        }

        if(count>max)
            max=count;
    }

    return max;
}

