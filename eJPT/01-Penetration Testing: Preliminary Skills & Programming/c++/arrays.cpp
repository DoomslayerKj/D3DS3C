#include<iostream>

using namespace std;


int main(int argc, char **argv)
{
	int a[20]; //Declaration
	int i;

	for(i=0;i<=19;i++)
	{
		a[i]=i;
	}

	for (i = 0 ; i<=19; i++)
	{
		cout <<"\n"<<a[i];
	}
	

	return 0;
}