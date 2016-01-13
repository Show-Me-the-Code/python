#include<stdio.h>
#include<string.h>
int main()
{
    char s[85];
    while(gets(s))
    {
        int en=0,space=0,num=0,other=0,i;//存放英文，空格，数字，其他字符的数量,以及计数器i
        int l=strlen(s);
        for(i=0;i<l;i++)
        {
            if((s[i]>='a'&&s[i]<='z')||(s[i]>='A'&&s[i]<='Z')) en++;
            else if(s[i]>='0'&&s[i]<='9') num++;
            else if(s[i]==' ') space++;
            else other++;
        }
        printf("%d %d %d %d\n",en,space,num,other);
    }
}
