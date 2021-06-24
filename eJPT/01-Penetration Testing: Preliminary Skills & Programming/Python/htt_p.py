import http.client
import sys
import os
import chardet
import urllib.request
import re



if __name__=='__main__':
    # if (len(sys.argv) < 3 or len(sys.argv) > 3):
    #     print(f"Usage: python3 {sys.argv[0]} PORT")
    #     sys.exit(1)
    host=str(sys.argv[1])
    port=80
    try:
        tes
        #connection=http.client.HTTPConnection(host,bytes(str(port),'utf-8'))
        connection=http.client.HTTPConnection(html.encode(host),port=80)

        connection.request('OPTIONS','/')
        response = connection.getresponse()
        print(f"Enabled Methods are: {response.getheader('allow')}")
        connection.close()
    except ConnectionRefusedError:
        print("Connection Refused!")

