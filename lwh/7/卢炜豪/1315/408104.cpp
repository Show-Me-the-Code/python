#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define SIZE 10005

//生成部分匹配表
void strcut(char *s,char* b,int l,int r) {
	int index = 0,i;
	int len = strlen(s);
	memset(b,0,sizeof(b));
	// printf("@%s   @%s\n",s,b);
	for(i=l,index=0;i<=r;i++,index++) {
		b[index] = s[i];
	}
	b[index] = '\0';
	//printf("@%s   @%s\n",s,b);
}
void match_table(char *s,int *a) {
	int i,j,res,temp;
	int len1 = strlen(s),len2;
	int front1,front2,rear1,rear2;
	char s0[SIZE],s1[SIZE],s2[SIZE];
	for(i=1;i<len1;i++) {
		strcut(s,s0,0,i);
		res = 0;
		temp = 0;
		front1 = rear1 = 0;
		front2 = rear2 = i;
		for(j=0;j<i;j++) {
			strcut(s,s1,front1,rear1++);
			strcut(s,s2,front2--,rear2);
			//printf("@%s @%s\n",s1,s2);
			if(strcmp(s1,s2)==0) {
				temp = strlen(s2);
				if(temp > res) {
					res = temp;
				}
			}
		}
		a[i] = res;
		//printf("match_table()...%s %s %s\n",s0,s1,s2);
	}
	a[0] = 0;
}

int main()
{
	int num_case;
	scanf("%d",&num_case);
	getchar();
	while(num_case--) {
		char s0[SIZE],s1[SIZE];
		int partcal_table[SIZE];
		int flag = 0;
		gets(s0);
		gets(s1);
		match_table(s1,partcal_table);

		int len_s0 = strlen(s0);
		int len_s1 = strlen(s1);
		int index_s0=0,index_s1=0;
		int i;
		/*
		for(i=0;i<len_s1;i++)
			printf("%d",partcal_table[i]);
		printf("\n");
		*/
		while(index_s0<len_s0) {
			//printf("index_s0=%d,index_s1=%d\n",index_s0,index_s1);
			if(s0[index_s0]==s1[index_s1]) {
				index_s0 = index_s0 + 1;
				index_s1 = index_s1 + 1;
				if(index_s1==len_s1) {
					flag=1;
					break;
				}
			}
			else if(s0[index_s0] != s1[index_s1]) {
				if(index_s1==0) {
					index_s0 = index_s0 + 1;
				}
				else if(index_s1!=0) {
					if(partcal_table[index_s1-1]>1 && index_s1!=1) {
						index_s0 = index_s0 + (index_s1 - partcal_table[index_s1-1]);
					}
				}
				index_s1=0;
			}

			if(index_s1==len_s1) {
				flag = 1;
			}
			else {
				flag = 0;
			}
		}
		if(flag==1) {
			printf("yes\n");
		}
		else {
			printf("no\n");
		}
	}
	//system("PAUSE");
}