#include<stdio.h>
#define maxn 105
int main()
{
    int m,n,a[maxn],b[maxn],c[maxn],d[maxn];//c[]储存交集
    while(scanf("%d %d",&m,&n)==2&&(m!=0&&n!=0))
    {
        int count=0,index=0;
        for(int i=0;i<m;i++)
            scanf("%d",&a[i]);
        for(int i=0;i<n;i++)
            scanf("%d",&b[i]);

        int q=0;
        for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
        {
            if(a[i]==b[j])
            {
                count++;
                c[q]=a[i];
                q++;

            }
        }
       // for(int i=0;i<q;i++)
      //  printf("c[%d]=%d\n",i,c[i]);
        if(count>=m) printf("NULL\n");
        else
        {
           int w=0;
           for(int i=0;i<m;i++)
           {
               int index=0;

               for(int j=0;j<q;j++)
               {
                   if(a[i]==c[j])
                   index++;
               }
           //    printf("index==%d\n",index);
               if(index==0)
                {
                    d[w]=a[i];
                    w++;
                  //  printf("w=%d\n",w);
                }
               //  printf("w=%d\n",w);
           }
        //   printf("w=%d\n",w);
         //  for(int i=0;i<w;i++) printf("%d ",d[i]);
           for(int i=1;i<w;i++)
           {
               int temp;
               if(d[i]>d[i-1])
               {
                   temp=d[i];
                   d[i]=d[i-1];
                   d[i-1]=temp;

               }

           }
           for(int i=w-1;i>=0;i--)
           {
               if(i!=0)
               printf("%d ",d[i]);
               else
                printf("%d\n",d[i]);

           }
         //  for(int i=0;i<w;i++) printf("%d ",d[i]);
        }
    }
}
