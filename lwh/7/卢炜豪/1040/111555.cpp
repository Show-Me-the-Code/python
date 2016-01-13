#include<stdio.h>
//void is7(int n);
void no7(int n);
int main()
{
    int n;
    while(scanf("%d",&n)!=0)
    {
        if(n%7==0)
        {
            printf("YES\n");
        }
        else if(n%7!=0)
        {
            no7(n);
        }
    }
}
void no7(int n)
{
  if(n<10)
  {
      printf("NO\n");
  }
  else if(n>=10)
  {

      int j=0;
      for(int i=1;i<=2;i++)
      {
         int w;
          w=n%10;
          if(w==0)
          {
              n=n/10;
              j++;
          }
          else if(w%7==0)
          {
              printf("YES\n");
              break;
          }
          else if(w%7!=0)
          {
              n=n/10;
              j++;
          }

      }
      if(j==2)
      {
          printf("NO\n");
      }
  }

}
