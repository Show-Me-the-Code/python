#include <cstdio>
#include <cstring>
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        int worknum,i,j=1,k,m;
        double rate=0,semblance;       //j是空格的下标
        scanf("%d",&worknum);
        getchar();   //读入单词数
        int book[100+5];            //标记句子空格的下标
        char s1[2200];
        char s2[2200];           //句子所在的字符串
        gets(s1);gets(s2);       //读入两个字符串
        int len=strlen(s1);     //字符串长度
        for(i=0;i<len;i++)
        {
            if(s1[i]==' ')
            {
                book[j]=i;
                j++;
            }
        }
       // printf("j=%d\n",j);
        book[0]=-1;book[j]=len;//空格的位置存储在数组book中
      //  for(int n=0;n<j;n++)
      //  printf("~=%d\n",book[n]);

        for(k=0,m=1;k<book[j-1];)
        {
            semblance=0;
        //    printf("%d %d\n",k,m);
            while(k<book[m])
            {
                if(s1[k]==s2[k])
                    semblance++;
                    k++;
            }
       //     printf("book[%d]=%d-book[%d]=%d->#%d\n",m,book[m],m-1,book[m-1],book[m]-book[m-1]-1);
            rate=rate+semblance/(book[m]-book[m-1]-1);
         //   printf("rate=%lf\n",rate);
            m+=1;
            k+=1;
        }
     //   printf("m=%d\n",m);
        semblance=0;
        for(k=book[m-1]+1;k<len;k++)
        {
            if(s1[k]==s2[k])
                semblance++;

        }
   //     printf("book[%d]=%d-book[%d]=%d->#%d\n",j,book[j],j-1,book[j-1],book[j]-book[j-1]-1);
        rate=rate+semblance/(book[j]-book[j-1]-1);
        printf("%.2lf%%\n",100*rate/worknum);

    }
}
