#include<stdio.h>
int main()
{
long long a,b,c,t;
scanf("%ld",&t);
while(t--)
{
scanf("%ld%ld%ld",&a,&b,&c);
if(a+b<=c || b+c<=a || a+c<=b)
printf("Wrong!!\n");
else
printf("OK\n");
}
}

/*
Author: Sabbir Shawon
*/