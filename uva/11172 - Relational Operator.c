#include<stdio.h>
int main()
{
  int a,b,t;
  scanf("%d",&t);
  while(t--)
  {
       scanf("%d %d",&a,&b);
       if(a<b)
       printf("<");
       else if(a>b)
       printf(">");
       else
       printf("=");
  }
  return 0;
}