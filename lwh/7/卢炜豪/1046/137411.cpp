#include<stdio.h>
#define maxn 20
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int n;int a[maxn][3],b[maxn];
        scanf("%d",&n);
        for(int j=0;j<n;j++)
        for(int k=0;k<3;k++)
        {
            scanf("%d",&a[j][k]);
            getchar();
        }

        int me=a[0][0]*60000+a[0][1]*1000+a[0][2];
      //  printf("me=%d\n",me);

        for(int l=0;l<n;l++)
       {
        b[l]=a[l][0]*60000+a[l][1]*1000+a[l][2];
     //   printf("b[%d]=%d\n",l,b[l]);
       }
        int temp;
        for(int m=1;m<n;m++)
        {
            for(int p=0;p<n-m;p++)
            {
                if(b[p]>b[p+1])
                {
                    temp=b[p];
                    b[p]=b[p+1];
                    b[p+1]=temp;
                }
            }
        }
      //  for(int t=0;t<n;t++) printf("%d\n",b[t]);
        for(int t=0;t<n;t++)
        {
            if(me==b[t]) {printf("%d\n",t+1);break;}
        }

    }
}
