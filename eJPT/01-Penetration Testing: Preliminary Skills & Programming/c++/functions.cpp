#include<iostream>

using namespace std; //<- STOP USING THIS,NOOB + DUMBASS


int CallByValue(int a, int b) //Call By Value
{
	return (a+b);
}

void swap_CallByReference(int &x, int &y)
{
	int temp;
	temp = x;
	x=y;
	y=temp;
}



int main(int argc, char **argv)
{
	int a,b,result;
	cout<<"Call By Value\n:";
	cout<<"Enter Two Numbers:"<<endl;
	cin>>a>>b;
	result=CallByValue(a,b);
	cout<<"Sum:"<<result<<endl;
	cout<<"After Funtion Call:"<<endl;
	cout<<"a="<<a<<" "<<"b="<<b<<"\n\n";

	cout<<"Call By Reference:"<<endl;
	cout<<"Before Swapping:";
	cout<<"a="<<a<<"b="<<b<<endl;
	swap_CallByReference(a,b);
	cout<<"After Funtion Call:"<<endl;
	cout<<"a="<<a<<" "<<"b="<<b<<"\n";


	

	return 0;
}