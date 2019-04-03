#include<stdio.h>
int main()
{
	int a,b,c;
	while((scanf("%d %d %d", &a, &b, &c))==3)
	if (b<=a || (b>a && c>a))
	{
		printf("Chocolate\n");
	}
	else
	{
		printf("Ice-cream\n");
	}	
}
