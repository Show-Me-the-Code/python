#include <cstdio>
#include <cstring>
char s1[400];
char s2[400];
int len;
void sort_(int n);
int cal(int n);
int main()
{
    int beadnum,max=0;
    scanf("%d",&beadnum);
    scanf("%s",s1);
    len=strlen(s1);int out;
    for(int i=0;i<len;i++)
    {
        sort_(i);
     //   printf("ii=%d\n",i);
        int out = cal(0);
        if(out>max)
            max=out;
    }
    printf("%d\n",max);

}
void sort_(int n)
{
    strcpy(s2,s1+n);
    strncat(s2,s1,n);
  //  printf("%s\n",s2);

}
int cal(int n)
{
    int ans=0;
    char t = s2[n];
   // printf("t=%c\n",t);
    for(int i = n;i<len;i++)
    {
       if(s2[i]==t||s2[i]=='w')
       {
           ans++;
       }
       else break;
    }
    char r = s2[len-1];
 //   printf("r=%c\n",r);
    for(int i = len-1;i>=0;i--)
    {
        if(s2[i]==r||s2[i]=='w')
            ans++;
        else break;
    }
    return ans;
}
