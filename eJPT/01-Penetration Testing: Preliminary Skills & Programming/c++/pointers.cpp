#include<iostream>

using namespace std;


int main(int argc, char **argv)
{

	//DataType *PointerName;
	//X = &y
	 int x = 10;
	 int y = 0;
	 
	 //Declaration
	 int *p1,*p2;

	 //Assignment
	 p1=&x;
	 p2=p1;
	 y=*p2; //Assigning Y value of variable stored in the address of P2 ,which is P1 -> X
	 *p2=5; //Memory Address pointed to by p2 is assigned 5 

	 cout << "p1: "<<p1 <<"\np2:"<< p2 <<endl;
	 cout <<"\ny: "<<y  <<"\nx: "<< x  <<endl;

	 cin.ignore();

	return 0;
}