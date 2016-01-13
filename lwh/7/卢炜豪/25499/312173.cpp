#include <cstdio>

#include <cstring>

int next1[3][2]={{1,0},{0,-1},{-1,0}};

int next2[3][2]={{0,-1},{-1,0},{0,1}};

int next3[3][2]={{-1,0},{0,1},{1,0}};

int next4[3][2]={{0,1},{1,0},{0,-1}};

int route[101][2];

int judge_x,judge_y;

int book[102][102];

char map[102][102];

int v;

void dfs(int x,int y,int dir);

int main()

{

    int n,m;

    while(scanf("%d %d",&n,&m)!=EOF)

    {

        if(n==0&&m==0)

            return 0;

        memset(book,0,sizeof(book));

        int startx,starty,endx,endy;

        for(int i=0;i<n;i++)

            scanf("%s",map[i]);//输入地图

            v=0;

       // printf("%c\n",map[2][3]);

        for(int i=0;i<n;i++)

        {

            for(int j=0;j<m;j++)

            {

                if(map[i][j]=='S')

                {

                    startx=i;

                    starty=j;

                   // printf("i=%d j=%d\n",i,j);

                }



            }

        }

        //printf("startx=%d starty=%d\n",startx,starty);//记录入口与出口的坐标

        route[v][0]=startx;route[v][1]=starty;

        v++;

        int direct;//direct=1表示向左，2表示向前，3表示向右,4表示向下

        //找出第一步可行的方向，传入dfs函数中

        if(map[startx][starty-1]=='.'||map[startx][starty-1]=='E')

        {

            book[startx][starty]=1;

            dfs(startx,starty,0);

        }

        else if(map[startx-1][starty]=='.'||map[startx][starty-1]=='E')

        {

            book[startx][starty]=1;

            dfs(startx,starty,1);

        }

        else if(map[startx][starty+1]=='.'||map[startx][starty-1]=='E')

        {

            book[startx][starty]=1;

            dfs(startx,starty,2);

        }

        else if(map[startx+1][starty]=='.'||map[startx][starty-1]=='E')

        {

            book[startx][starty]=1;

            dfs(startx,starty,3);

        }



    }

}

void dfs(int x,int y,int dir)

{

    int last_step_x=x,last_step_y=y;

    if(map[x][y]=='E')

    {

        for(int i=0;i<v;i++)

            printf("%d %d\n",route[i][0]+1,route[i][1]+1);

        return;

    }

    for(int i=0;i<3;i++)

    {

        if(dir==0)

        {

            int cmpx=x+next1[i][0],cmpy=y+next1[i][1];

            if(cmpx<0||cmpy<0||book[cmpx][cmpy]==1||map[cmpx][cmpy]=='#')

                continue;

            x+=next1[i][0];

            y+=next1[i][1];

            judge_x=x-last_step_x;

            judge_y=y-last_step_y;

            if(judge_x==0&&judge_y==-1)

                dir=0;

            else if(judge_x==-1&&judge_y==0)

                dir=1;

            else if(judge_x==0&&judge_y==1)

                dir=2;

            else if(judge_x==1&&judge_y==0)

                dir=3;

       //     printf("i=%d x=%d y=%d last_step_x=%d last_step_y=%d judge_x=%d judge_y=%d dir=%d map[%d][%d]=%c\n",i,x,y,last_step_x,last_step_y,judge_x,judge_y,dir,x,y,map[x][y]);

            book[x][y]=1;

            route[v][0]=x;

            route[v][1]=y;

            v++;

            dfs(x,y,dir);

            book[x][y]=0;

        }

        else if(dir==1)

        {

            int cmpx=x+next2[i][0],cmpy=y+next2[i][1];

            if(cmpx<0||cmpy<0||book[cmpx][cmpy]==1||map[cmpx][cmpy]=='#')

                continue;

            x+=next2[i][0];

            y+=next2[i][1];

            judge_x=x-last_step_x;

            judge_y=y-last_step_y;

            if(judge_x==0&&judge_y==-1)

                dir=0;

            else if(judge_x==-1&&judge_y==0)

                dir=1;

            else if(judge_x==0&&judge_y==1)

                dir=2;

            else if(judge_x==1&&judge_y==0)

                dir=3;

       //     printf("i=%d x=%d y=%d last_step_x=%d last_step_y=%d judge_x=%d judge_y=%d dir=%d map[%d][%d]=%c\n",i,x,y,last_step_x,last_step_y,judge_x,judge_y,dir,x,y,map[x][y]);

            book[x][y]=1;

            route[v][0]=x;

            route[v][1]=y;

            v++;

            dfs(x,y,dir);

            book[x][y]=0;

        }

        else if(dir==2)

        {

            int cmpx=x+next3[i][0],cmpy=y+next3[i][1];

            if(cmpx<0||cmpy<0||book[cmpx][cmpy]==1||map[cmpx][cmpy]=='#')

                continue;

            x+=next3[i][0];

            y+=next3[i][1];

            judge_x=x-last_step_x;

            judge_y=y-last_step_y;

            judge_x=x-last_step_x;

            judge_y=y-last_step_y;

            if(judge_x==0&&judge_y==-1)

                dir=0;

            else if(judge_x==-1&&judge_y==0)

                dir=1;

            else if(judge_x==0&&judge_y==1)

                dir=2;

            else if(judge_x==1&&judge_y==0)

                dir=3;

        //    printf("i=%d x=%d y=%d last_step_x=%d last_step_y=%d judge_x=%d judge_y=%d dir=%d map[%d][%d]=%c\n",i,x,y,last_step_x,last_step_y,judge_x,judge_y,dir,x,y,map[x][y]);

            book[x][y]=1;

            route[v][0]=x;

            route[v][1]=y;

            v++;

            dfs(x,y,dir);

            book[x][y]=0;

        }

        else if(dir==3)

        {

            int cmpx=x+next4[i][0],cmpy=y+next4[i][1];

            if(cmpx<0||cmpy<0||book[cmpx][cmpy]==1||map[cmpx][cmpy]=='#')

                continue;

            x+=next4[i][0];

            y+=next4[i][1];

            judge_x=x-last_step_x;

            judge_y=y-last_step_y;

            if(judge_x==0&&judge_y==-1)

                dir=0;

            else if(judge_x==-1&&judge_y==0)

                dir=1;

            else if(judge_x==0&&judge_y==1)

                dir=2;

            else if(judge_x==1&&judge_y==0)

                dir=3;

           // printf("i=%d x=%d y=%d last_step_x=%d last_step_y=%d judge_x=%d judge_y=%d dir=%d map[%d][%d]=%c\n",i,x,y,last_step_x,last_step_y,judge_x,judge_y,dir,x,y,map[x][y]);

            book[x][y]=1;

            route[v][0]=x;

            route[v][1]=y;

            v++;

            dfs(x,y,dir);

            book[x][y]=0;

        }

    }

    return;

}

#include
//s
//*
asd
/*
asdlkdfgskgj
*/