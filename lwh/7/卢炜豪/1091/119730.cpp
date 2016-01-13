#include<stdio.h>
int main()
{
    int m,n;
    while(1)
    {
        scanf("%d %d",&m,&n);
        if(m==0&&n==0) break;

        int a[105],b[105];
        for(int i=0;i<m;i++)
        scanf("%d",&a[i]);
        for(int j=0;j<n;j++)
        scanf("%d",&b[j]);

        int count=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(a[i]==b[j])
                    count++;
            }
        }

         int c[count],index=0;
         for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(a[i]==b[j])
                {
                    c[index]=a[i];
                    index++;
                }
        }
        }

       int num=m-index+1;
       int last[num],temp=0;

       for(int i=0;i<m;i++)
       {
           for(int j=0;j<index;j++)
           {
               if(a[i]!=c[j])
               {
                   last[temp]=a[i];
                   temp++;
               }
           }
       }
      if(index==m) printf("NULL");
      else for(int i=0;i<temp;i++)
       {
           if(i==temp-1) printf("%d",last[i]);
            else printf("%d ",last[i]);
       }
       printf("\n");

}
}
