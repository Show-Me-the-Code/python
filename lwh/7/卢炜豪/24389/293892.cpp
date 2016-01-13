#include <cstdio>
long long int arr[2222];
long long int sum=0,add=1;
void cal_l(int f,int s);
void cal_r(int f,int s);
int main()
{
    int N;arr[0]=0;
    scanf("%d",&N);
for(int i=1;i<=N;i++)
        arr[i]=i;  //1-N存进数组
    if(N%2!=0)
    {cal_l(1,N/2+1);
    cal_r(N/2+2,N);
    }
    else if(N%2==0)
    {cal_l(1,N/2);
    cal_r(N/2+1,N);
    }
    printf("%d\n",sum);
}
void cal_l(int f,int s)
{if(s-f+1==2||s-f==0)
       {if(s-f+1==2)
           sum=sum+arr[f]*arr[s];
           if(s-f==0)
            arr[s]=1;
            return;
       }
    else
    {if((s-f+1)%2!=0)
        {
            cal_l(f,(s-f+1)/2+f);
            cal_r((s-f+1)/2+f+1,s);}
        if((s-f+1)%2==0)
        {
            cal_l(f,((s-f+1)/2)-1+f);
            cal_r(((s-f+1)/2)+f,s);
        }
        return ;
    }
}
void cal_r(int f,int s)
{if(s-f+1==2||s-f==0)
       {
           if(s-f+1==2)
           {
            sum=sum+arr[f]*arr[s];}
           if(s-f==0)
            arr[s]=1;
            return ;
       }
    else
    {
        if((s-f+1)%2!=0)
        {
            cal_l(f,(s-f+1)/2+f);
            cal_r((s-f+1)/2+f+1,s);
        }
         if((s-f+1)%2==0)
        {
            cal_l(f,((s-f+1)/2)-1+f);
            cal_r(((s-f+1)/2)+f,s);
        }
        return;}
}
