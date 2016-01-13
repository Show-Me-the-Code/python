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
    len=strlen(s1);int max,ans=0,index;
    for(int i=0;i<len;i++)
    {
        sort_(i);
        char head=s2[0];
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
        char tail=s2[len-1];
        for(int j=len-1;j>index;j--)
        {
            if(s2[j]==tail||s2[j]=='w')
                max++;
            if(s2[j]!=tail&&s2[j]!='w')
                break;
        }
        if(max>ans)
            ans=max;
    }
    printf("%d\n",ans);

}
void sort_(int n)
{
    strcpy(s2,s1+n);
    strncat(s2,s1,n);
    //printf("%s\n",s2);

}
