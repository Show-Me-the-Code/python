#include <stdio.h>
#include <string.h>


#define max 100005

int prime[max];
int book[max];
int check[max];

int main()
{
    int tot=0;
    memset(check,0,sizeof(check));
    memset(book,1,sizeof(book));
    for(int i=2;i<max;++i)
    {
        if(check[i]==0)
        {

            prime[tot]=i;
            book[i]=0;
     //       printf("tot=%d %d\n",tot,prime[tot]);
            tot++;
        }
        for(int j=0;j<tot;++j)
        {
            if(i*prime[j]>max)
                break;
            check[i*prime[j]]=1;
            if(i%prime[j]==0)
                break;
        }
    }
    /*    for(int i=0;i<561;i++)
        printf("check[%d]=%d prime[%d]=%d book[%d]=%d\n",i,check[i],i,prime[i],i,book[i]);
            printf("q=%d\n",q);
            */
     //       printf("%d\n",prime[3]);
    //素数表构建完成，接下来进行歌德巴赫输出

    int n,i,j,left1,right1;
	while(scanf("%d",&n)!=EOF)
    {
       int left,right,plus;
       for(left=3,right=n-left;left<=n/2;left++,right=n-left)
       {
          // printf("left=%d right=%d\n",left,right);
           if(book[left]==0&&book[right]==0&&left+right==n)
           {
               left1=left;
               right1=right;
             //  printf("~plus=%d and %d %d\n\t",plus,left,right);
           }
       }
       printf("%d %d\n",left1,right1);

    }


}
