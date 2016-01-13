#include<stdio.h>
int main()
{

    char a,b;int i;
    while(1)
    {
        int temp=0,temp1=0;
       for(;(a=getchar())!='\n';)
       {
           if(a=='a'||a=='e'||a=='i'||a=='o'||a=='u'||a=='A'||a=='E'||a=='I'||a=='O'||a=='U')
            temp++;
       }
       for(i=0;(b=getchar())!='\n';i++)
       {
           if(b=='a'||b=='e'||b=='i'||b=='o'||b=='u'||b=='A'||b=='E'||b=='I'||b=='O'||b=='U')
            temp1++;
       }
      // printf("%d %d\n",temp,temp1);
      if(temp>temp1) printf("a>b\n");
      else if(temp<temp1) printf("a<b\n");
      else printf("a=b\n");
    }

}
