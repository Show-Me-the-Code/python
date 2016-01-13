#include<stdio.h>
#define maxn 10000
#define ch 65
int main()
{
    int n;
    char s[maxn][ch];
    int price[maxn];
    int max=0,min=0;
    scanf("%d",&n);
    scanf("%s",&s[0][0]);
    getchar();
    scanf("%d",&price[0]);
    for(int i=1;i<n;i++)
    {

        //int j;

        scanf("%s",&s[i][0]);
        getchar();
        scanf("%d",&price[i]);

        if(price[i]>price[max]) max=i;
        if(price[i]<price[min]) min=i;

    }
    printf("%s %s\n",&s[max][0],&s[min][0]);
}
