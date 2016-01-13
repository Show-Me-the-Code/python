#include <cstdio>
#include <cstring>
char s1[400];
char s2[400];
int len;
void sort_(int n);
int cal(int n);
int main()
{
    int beadnum;
    scanf("%d",&beadnum);
    getchar();
    gets(s1);
  //  printf("\n");
    len=strlen(s1);int max,ans=0,index=len-1;
    for(int i=0;i<len;i++)
    {
        sort_(i);
        index=len-1;
        char head=s2[0];//printf("head=%c ",head);
        max=0;
        for(int j=0;j<len;j++)
        {
            if(s2[j]==head||s2[j]=='w')
                max++;
            if(s2[j]!=head&&s2[j]!='w')
            {
                index=j; //记录前面遍历时跳出去的下标
                break;
            }
        }
      //  printf("max1=%d index=%d ",max,index);
        char tail=s2[len-1];
        if(index==len-2)
            max++;
        for(int j=len-1;j>index;j--)
        {
            if(s2[j]==tail||s2[j]=='w')
                max++;
            if(s2[j]!=tail&&s2[j]!='w')
                break;
        }
      //  printf("max=%d\n\n",max);
        if(max>ans)
            ans=max;
    }
    printf("%d\n",ans);

}
void sort_(int n)
{
    strcpy(s2,s1+n);
    strncat(s2,s1,n);
  //  printf("%s\n",s2);

}
