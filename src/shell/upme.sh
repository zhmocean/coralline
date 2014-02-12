#! /bin/sh


IP_SERVER=checkip.dyndns.com
IP_SKIP="Address: "
PASSWORD=mypassword
UP_SERVER=cloud.tangcu.biz/up
UP_TYPE=home


IP=`curl "$IP_SERVER" | grep "$IP_SKIP"| awk -F"$IP_SKIP" '{print $2}' | awk -F'<' '{print $1}'`
echo my IP: $IP
RESP=`curl "$UP_SERVER/$UP_TYPE?pwd=$PASSWORD&type=$UP_TYPE&ip=$IP"`
echo "$RESP"