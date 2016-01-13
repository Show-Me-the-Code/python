#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    char x[80]={0},*endptr,d[80];
    while(gets(x)!='\0')
    {
        //getchar();
        int l=strlen(x);int w=0;
        for(int i=0;i<l;i++)
        {
            if((x[i]>='0'&&x[i]<='9')||(x[i]>='a'&&x[i]<='f')||(x[i]>='A'&&x[i]<='F'))
            {
                d[w]=x[i];
                w++;
            }

        }
        if(w==0) printf("0\n");
       // for(int i=0;i<w;i++) printf("%c",d[i]);
       // printf("\n");
      else{

       int a;
       a=(int)strtol(d,&endptr,16);
       printf("%d\n",a);
      }
    }
}
