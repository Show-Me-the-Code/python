#include<stdio.h>
int main()
{
    int m,n,i,j,k,l;char op;
    scanf("%d %d %c",&m,&n,&op);
    int a[m][n],b[m][n],c[m][n];
    for(i=0;i<m;i++)
      for(j=0;j<n;j++)
        scanf("%d",&a[i][j]);

    for(k=0;k<m;k++)
      for(l=0;l<n;l++)
       scanf("%d",&b[k][l]);

   if(op=='+')
   {
      for(int w=0;w<m;w++)
   {
        for(int q=0;q<n;q++)
        {
            c[w][q]=a[w][q]+b[w][q];
            if(q==n-1) printf("%d",c[w][q]);
            else printf("%d ",c[w][q]);
        }
        printf("\n");

   }

   }
   else if(op=='-')
   for(int w=0;w<m;w++)
   {
        for(int q=0;q<n;q++)
        {
            c[w][q]=a[w][q]-b[w][q];
            if(q==n-1) printf("%d",c[w][q]);
            else printf("%d ",c[w][q]);
        }
        printf("\n");

   }



}
