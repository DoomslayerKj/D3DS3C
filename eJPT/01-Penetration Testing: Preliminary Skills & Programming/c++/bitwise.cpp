#include<iostream>

using std::cout;
using std::cin;
using std::endl;

int main(int argc,char **argv)
{

	int x,y;
	cout << "Enter X:";
	cin >> x;
	cout << "Enter Y:";
	cin>> y;

	int bitwiseAnd = x & y; //bitwise and
	int bitwiseOR = x | y;  //bitwise or
	cout << "\nAND:"<<bitwiseAnd;
	cout << "\nOR:"<<bitwiseOR;



	return 0;
}