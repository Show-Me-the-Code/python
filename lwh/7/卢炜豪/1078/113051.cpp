#include<stdio.h>
#include<math.h>
int isprime(int sum);
int main()
{
    int n;int x,y;
    while(1)
    {
       // if(x==0&&y==0) break;
        int sum;int index;
        scanf("%d %d",&x,&y);
         if(x==0&&y==0) break;
        for(int i=x;i<=y;i++)
        {

            sum=pow(i,2)+i+41;
          // int l=sqrt(sum);
           // printf("%d\n",l);
            index=isprime(sum);

        } if(index==(int)(sqrt(sum)-1)) printf("OK\n");
        else printf("Sorry\n");
          //if(d!=0) printf("Sorry\n");
    }
    return 0;
}
int isprime(int sum)
{
    int t=0,q=0;
    for(int d=2;d<=sqrt(sum);d++)
    {

        if(sum%d==0) q++;
        if(sum%d!=0) t++;


    }
    //if(q!=0) printf("Sorry\n");
    return t;
}
