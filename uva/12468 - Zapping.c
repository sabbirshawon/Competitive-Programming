#include<stdio.h>
int main()
{
    int a,b,t;
    while(scanf("%d %d",&a,&b)==2 && (a!=-1 && b!=-1))
        {
        t=abs(a-b);

        if(t>50)
            t=100-t;

        printf("%d\n",t);
    }
    return 0;
}
