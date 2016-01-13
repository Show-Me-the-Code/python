#include<stdio.h>
#define maxn 20
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        int n;
        scanf("%d",&n);
        int a[maxn][3];

        for(int j=0;j<n;j++)
        {
            for(int k=0;k<3;k++)
            {
                scanf("%d",&a[j][k]);
                getchar();
            }
        }
       /* for(int j=0;j<n;j++)
        for(int k=0;k<3;k++)
        printf("%d ",a[j][k]);
        printf("\n");*/
        int a0=a[0][0],a1=a[0][1],a2=a[0][2],num=0,count=0,count1=0,count2=0;

        for(int j=1;j<n;j++)     //检查第一列是否相等
        {
            if(a[j][0]==a[j-1][0])
            count++;
        }
       // printf("①count==%d,n==%d\n",count,n);
        if(count!=n-1)       //如果不相等
        {
        for(int j=0;j<n-1;j++)
        {
            for(int k=1;k<n;k++)
            {
                if(a[k][0]<a[k-1][0])
                {
                    int temp;
                    temp=a[k][0];
                    a[k][0]=a[k-1][0];
                    a[k-1][0]=temp;
                }
            }
        }
        for(int j=0;j<n;j++)
        {
            if(a0==a[j][0]){num=j+1;break;}
        }
        printf("%d\n",num);
        }


       else if(n==count+1)    //如果相等
       {

           for(int j=1;j<n;j++)
           {
               if(a[j][1]==a[j-1][1])
                count1++; //检查第二组数据是否相等
           }
          // printf("②count1==%d,n==%d\n",count1,n);
           if(count1!=n-1)                      //如果第二组数据不相等
           {
            for(int j=0;j<n-1;j++)
            {
            for(int k=1;k<n;k++)
            {
                if(a[k][1]<a[k-1][1])
                {
                    int temp;
                    temp=a[k][1];
                    a[k][1]=a[k-1][1];
                    a[k-1][1]=temp;
                }
            }
            }
        for(int j=0;j<n;j++)
        {
            if(a1==a[1][j]){ num=j+1;break;}
        }
       // printf("②count1==%d,n==%d\n",count1,n);
        printf("%d\n",num);
           }

           else if(count1==n-1)  //第二组数据全部相等
           {
               for(int m=0;m<n-1;m++)
            {
            for(int q=1;q<n;q++)
            {
                if(a[q][2]<a[q-1][2])
                {
                    int temp;
                    temp=a[q][2];
                    a[q][2]=a[q-1][2];
                    a[q-1][2]=temp;
                }
            }
             for(int h=0;h<n;h++)
        {
            if(a2==a[h][2]){ num=h+1;break;}
        }
         //printf("!%d\n",num);
            }printf("%d\n",num);
           }
       }

    }
}

