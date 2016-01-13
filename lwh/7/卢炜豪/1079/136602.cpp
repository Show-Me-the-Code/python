#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    char x[80]={0},*endptr,d[80];
    while(scanf("%s",x)!=EOF)
    {
        int l=strlen(x);int w=0;int num=0;
        for(int i=0;i<l;i++)
        {
            if((x[i]>='0'&&x[i]<='9')||(x[i]>='a'&&x[i]<='f')||(x[i]>='A'&&x[i]<='F'))
            {
                d[w]=x[i];
                w++;
            }
             if(x[i]>='0'&&x[i]<='9')
             {
                 num++;
             }

        }
       d[w]='\0';
       if(num==0&&w==0) printf("0\n");
      // else if(num==0) printf("0\n");
       else{

       int a;
       a=(int)strtol(d,&endptr,16);
       printf("%d\n",a);
       fflush(stdin);

      }


    }
}
