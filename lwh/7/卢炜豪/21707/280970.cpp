/*先遍历一遍，用两个变量记录出现连续两个数字出现的次数，
  依次更迭替换最大值，并用一个数组来记录
  */
#include<stdio.h>

int main()
{
   freopen("test.txt","r",stdin);
    int N,b[1002],max=0,a,temp,q,k;//max记录
    scanf("%d",&N);

    for(int i=0;i<N;i++)
        scanf("%d",&b[i]);//写入牛的品种信息到数组b[i]中；

    int i=1;
    int count=0;
    while(i<N-1)
    {
        q=0;
        count=0;
        if(b[i-1]==b[i+1])
        {
        temp=b[i];
        for(int j=i-1;;)
        {
            if(b[j]==b[i-1]||b[j]==temp)
            {
                count++;
                if(b[j]==temp)
                    q++;
            }
            else //if((b[j]!=b[i-1]&&b[j]!=temp)&&j>N-1)
                break;

            j++;

        }
        count=count-q;
        if(count>max)
        {
            max=count;
            k=max;
           //  printf("count=%d max=%d\n",count,max);
        }
        }
         i++;
    }

    printf("%d\n",k);
}
