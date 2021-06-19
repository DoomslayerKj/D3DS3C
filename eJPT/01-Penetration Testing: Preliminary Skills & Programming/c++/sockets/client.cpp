#include<iostream>
#include<dirent.h>


using namespace std; //<- STOP USING THIS,NOOB + DUMBASS

void printCurrentDirectory()
{
	struct dirent *d; //creating a dirent structure to save data from dir* functions

	DIR *dr; //directory discriptor

	dr=opendir(".");

	if(dr != NULL)
	{
		cout<<"List of Files and Folders:\n";
		
		for(d=readdir(dr);d!=NULL;d=readdir(dr))
		{
			cout<<d->d_name<<endl; //print dir name(d_name) member from dirent structure
		
		}
		closedir(dr);

	}

else
	{
		cout<<"\nError Occured!";
		exit(1);
	}
}

void Test_sendTCP(string a)
{
	cout<<a;
}



int main(int argc, char **argv)
{

	string b = printCurrentDirectory();
	Test_sendTCP(b);
	cout<<endl;
	return 0;
}