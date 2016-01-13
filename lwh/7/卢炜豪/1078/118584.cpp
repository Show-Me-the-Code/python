#include<stdio.h>
#include<math.h>
int isprime(int v);
int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n))
    {
       if(m==0&&n==0) break;
       int i,w,z,temp;
       int num=n-m+1;
       int a[num];

       for(i=0;m<=n;m++,i++)
       a[i]=m;



       for(i=0;i<num;i++)
       {
           int count=0;
           w=a[i]*a[i]+a[i]+41;
           z=isprime(w);
           if(z==1) count++;
       //    printf("a[%d]=%d,count=%d z=%d \n",i,w,count,z);
           temp=count;
       }
       if(temp==num)
       {printf("Sorry\n");
     //  printf("temp=%d,num=%d\n",temp,num);
       }
       else if(temp==0)
       {printf("Ok\n");
      // printf("temp=%d,num=%d\n",temp,num);
       }
}
}
int isprime(int v)
{
   int n,s,i;
   s=sqrt(v);
       for(n=1;n<=s;n++)
       {
            if(v%n==0)
            i++;
        }

        if(i!=1)
        return 0;
    else
        return 1;
    i=0;
}
