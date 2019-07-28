#include<stdio.h>

int main()
{
    long long int a1,t1,a2,t2,v1,v2;
    scanf("%lld %lld", &a1, &t1);
    scanf("%lld %lld", &a2, &t2);
    v1=a1*t1;
    v2=a2*t2;
    if(v1>v2)
    {
        printf("Mustafizur Rahman\n");
    }
    else
    {
        printf("Mitchell Starc\n");
    }
    return 0;
}
