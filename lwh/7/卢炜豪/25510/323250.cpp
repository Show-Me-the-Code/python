#include <cstdio>
#include <cstring>
char Map[55][55];
int book[55][55];
int hor(int i,int j)
{
    if(Map[i][j]=='.'){
        int index = 1;
        for(int k=j-1 ; k>=0 ; k--){
            if(Map[i][k]!='#'){
                index = 0;
                break;
            }
        }
        if((j-1<0||index==1)&&(Map[i][j+1]=='.'&&Map[i][j+2]=='.'))
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
    int index = 1;
	for(int k=i-1 ; k>=0 ; k--){
        if(Map[k][j]!='#'){
            index = 0;
            break;
        }
	}
	if((i-1<0||index==1)&&(Map[i+1][j]=='.'&&Map[i+2][j]=='.'))
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
	int num = 0;
	//freopen("7","r",stdin);
	scanf("%d %d",&N,&M);

	for(int i=0 ; i<N; i++){
		scanf("%s",Map[i]);
	}

	for(int i=0; i<N ; i++){
        for(int j=0 ; j<M; j++){
            if(hor(i,j)){
				//printf("~\n");
                book[i][j]=1;
				num++;
            }
            else if(ver(i,j)){
				//printf("~\n");
                book[i][j]=1;
				num++;
            }
        }
	}
	printf("%d\n",num);
	for(int i=0 ; i<N ; i++){
		for(int j=0; j<M ;j++){
			if(book[i][j])
				printf("%d %d\n",i+1,j+1);
		}
	}
}
