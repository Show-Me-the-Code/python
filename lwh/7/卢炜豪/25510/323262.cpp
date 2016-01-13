#include <cstdio>
#include <cstring>
char Map[55][55];
int book[55][55];
int hor( int i, int j)
{
    if(Map[i][j]=='.'){
        if((j-1<0||Map[i][j-1]=='#')&&(Map[i][j+1]=='.'&&Map[i][j+2]=='.'))
            return 1;
        else
            return 0;
            }
        else
            return 0;
}
int ver(int i,int j)
{
    if(Map[i][j]=='.'){
	if((i-1<0||Map[i-1][j]=='#')&&(Map[i+1][j]=='.'&&Map[i+2][j]=='.'))
        return 1;
    else
        return 0;
    }
    else
        return 0;
}
int main()
{
	 int N,M;
	 int  num = 0;
	//freopen("7","r",stdin);
	scanf("%d %d",&N,&M);

	for( int i=0 ; i<N; i++){
		//for(long long int j=0 ; j<M; j++){
            scanf("%s",Map[i]);
		//}
	}

	for(int i=0; i<N ; i++){
        for(int j=0 ; j<M; j++){
            if(hor(i,j)){
                book[i][j]=1;
				num++;
            }
            else if(ver(i,j)){
                book[i][j]=1;
				num++;
            }
        }
	}
	printf("%d\n",num);
	for( int i=0 ; i<N ; i++){
		for( int j=0; j<M ;j++){
			if(book[i][j])
				printf("%d %d\n",i+1,j+1);
		}
	}
}
