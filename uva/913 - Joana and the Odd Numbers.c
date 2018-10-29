#include<stdio.h>
int main()
{
    long long n,m,s,i,sum;
    while(scanf("%lld",&n)==1)
    {
        sum=0;
        m=(n/2)+1;
        s=n*m+(m-1);
        for(i=1; i<=3; i++)
        {
            sum=sum+s;
            s=s-2;
        }
        printf("%lld\n",sum);
    }
    return 0;
}