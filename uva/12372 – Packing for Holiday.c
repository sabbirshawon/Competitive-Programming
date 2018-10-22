#include<stdio.h>
int main()
{
    int a,b,c,t,i;
    while(scanf("%d",&t)==1)
    {
        for(i=1;i<=t;i++)
        {
            scanf("%d%d%d",&a,&b,&c);
            if(a<=20 && b<=20 && c<=20)
            printf("Case %d: good\n",i);
            else
            printf("Case %d: bad\n",i);
        }
    }
    return 0;
}