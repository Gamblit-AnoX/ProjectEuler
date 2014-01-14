#include<stdio.h>
#include<math.h>

int main(void)
{
	int sum_square=0;
	int square_somme=0;
	
	for(int i=1;i<=100;i++)
	{
		sum_square+=pow(i,2);
	}
	for(int j=1;j<=100;j++)
	{
		square_somme+=j;
	}
	square_somme=pow(square_somme,2);
	printf("%d",square_somme-sum_square);

}




