#include<stdio.h>
#include<string.h>
#define mm 1005
int main()
{
    char a[mm],b[mm];
    while(gets(a))
    {
        int temp=0,temp1=0;
        gets(b);
        int l=strlen(a);
        for(int i=0;i<l;i++)
        {
            if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u') temp++;
            if(b[i]=='a'||b[i]=='e'||b[i]=='i'||b[i]=='o'||b[i]=='u') temp1++;
        }
          if(temp>temp1) printf("a>b\n");
      else if(temp<temp1) printf("a<b\n");
      else printf("a=b\n");
    }
    return 0;


}
