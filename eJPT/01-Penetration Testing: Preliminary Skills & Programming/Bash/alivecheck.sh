#!/bin/bash
for protocol in 'http://' 'https://'; do
	while read line;
	do
		
		response_code=$(timeout 5 curl -L --write-out "%{http_code}" --output /dev/null   --silent --insecure $protocol$line)
		if [ "$response_code" == "000" ];then
			echo "$protocol$line: not responding"
		else
			echo "$protocol$line: HTTP $response_code"
			echo $protocol$line: $responsecode > alive.txt
		fi
	done < domains.txt
done