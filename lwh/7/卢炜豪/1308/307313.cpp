#include <cstdio>
#include <cstring>
struct loc
{
    int x,y;
};
int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n)==2)
    {
        int startx,starty,endx,endy,tx,ty,flag=0;
        struct loc que[3000];
        char map[52][52];int book[52][52];
        if(m==0&&n==0)
            break;
        memset(book,0,sizeof(book));
        memset(map,'\0',sizeof(map));
        scanf("%d %d %d %d",&startx,&starty,&endx,&endy);
      //  printf("m=%d n=%d\n",m,n);
        int next[4][2]={{0,1},{1,0},{0.-1},{-1,0}};
        for(int i=0;i<m;i++)
        {
            scanf("%s",map[i]);
        }
        if(m==1&&n==1&&map[0][0]=='.')
            flag=1;
      //  printf("!!%c\n",map[1][1]);
      //  for(int i=0;i<m;i++)
     //   {
     //       for(int j=0;j<n;j++)
     //           printf("%c",map[i][j]);
     //       printf("\n");
     //   }

        int head=0,tail=0;
        que[tail].x=startx;que[tail].y=starty;
        book[startx][starty]=1;
        tail++;
        while(tail>head)
        {
            for(int i=0;i<4;i++)
            {
           //     printf(">\n");
                tx=que[head].x+next[i][0];
                ty=que[head].y+next[i][1];

                if(tx<0||tx>m-1||ty<0||ty>n-1)
                    continue;
         //       printf("tx=%d ty=%d\n",tx,ty);
                if(map[tx][ty]=='.'&&book[tx][ty]==0)
                {
               //     printf("tx=%d ty=%d map[%d][%d]=%c\n",tx,ty,tx,ty,map[tx][ty]);
                    book[tx][ty]=1;
                    que[tail].x=tx;
                    que[tail].y=ty;
                    tail++;
                   // printf("tx=%d ty=%d\n",tx,ty);
                }
                if(tx==endx&&ty==endy&&map[tx][ty]=='.')
                {
                  //  printf("~~%d %d %d %d\n",tx,ty,endx,endy);
                    flag=1;
                    break;
                }
            }
                if(flag==1)
                    break;
                    head++;
            }
            if(flag==1)
                printf("YES\n");
            else
                printf("NO\n");
    }
    return 0;
}
