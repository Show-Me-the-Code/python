/*先遍历一遍，用两个变量记录出现连续两个数字出现的次数，
  依次更迭替换最大值，并用一个数组来记录
  */
#include<stdio.h>

int main()
{
   // freopen("data.txt","r",stdin);
    int N,b[1002],max=0,temp,q,k=0,a[4]={0,0,0,0};//max记录
    scanf("%d",&N);
    for(int i=0;i<N;i++)
        scanf("%d",&b[i]);//写入牛的品种信息到数组b[i]中；


    if(N==1)
        printf("%d\n",1);

    if(N==2)
    {
        if(b[0]==b[1])
        printf("%d\n",2);
        else printf("%d\n",1);
    }
    else if(N>=3)
    {

    int i=1;
    int count;
    if(b[0]==b[1])
    {
        for(int w=0;w<N;w++)
        {
            if(b[w]==b[0])
                k++;
                //printf("%d\n",k);
            if(b[w]!=b[0])
                break;
        }
        if(k==N)
        k=k-1;
    else
        a[0]=k;

    }
    else if(b[N-1]==b[N-2])
    {
        for(int w=N-1;;w--)
        {
            if(b[w]==b[N-1])
                k++;
            else if(b[w]!=b[N-1]||w<0)
                break;
        }
        if(k==N)
        k=k-1;
    else
        a[1]=k;

    }
    else
    while(i<N-1)
    {
        q=0;
        count=0;
        if(i==1)
        {

        for(int e=0;e<N-1;e++)
        {

            if(b[e]==b[e+1])
            {
                for(int r=e;r<N;r++)
                {
                    if(b[r]==b[e])
                        k++;
                    else break;
                }
     //           printf("%d\n",k);
            }
            if(k>max)
                max=k;
                k=0;
        }
        a[3]=max;
         max=0;
        k=0;
        }
        if(b[i-1]==b[i+1])
        {
        temp=b[i];
        for(int j=i-1;;)
        {
            if(b[j]==b[i-1]||b[j]==temp)
            {
                count++;
                if(b[j]==temp&&temp!=b[i-1])
                    q++;
            }
            else //if((b[j]!=b[i-1]&&b[j]!=temp)&&j>N-1)
                break;

            j++;

        }
      //  printf("count=%d q=%d\n",count,q);
        count=count-q;
        if(count>max)
        {
            max=count;
            k=max;
          //   printf("count=%d max=%d\n",count,max);
        }
        }
         i++;

    }
     a[2]=k;
    // printf("a[0]=%d a[1]=%d a[2]=%d a[3]=%d\n",a[0],a[1],a[2],a[3]);
     for(int m=1;m<4;m++)
     {
         for(int n=0;n<4-m;n++)
         {
             if(a[n]>a[n+1])
             {
                 int t=a[n];
                 a[n]=a[n+1];
                 a[n+1]=t;
             }
         }
     }
     if(a[3]==0)
        printf("%d\n",1);
     else
     printf("%d\n",a[3]);

    }

}
