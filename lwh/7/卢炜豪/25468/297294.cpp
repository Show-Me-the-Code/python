#include <cstdio>
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        int k;
        scanf("%d",&k);
        if(k%4==0||k%6==0)
            printf("Oh,yes.\n");
        else
        {

                printf("Oh,my dear.\n");
        }
      //  T--;
    }
    return 0;
}
