#!/bin/bash

IP_SERVER="cloud.tangcu.biz/me"
IP_SKIP="Address: "
PASSWORD="mypassword"
UP_SERVER="cloud.tangcu.biz/up"
UP_TYPE="home"


IP=$(curl -s "${IP_SERVER}" | grep "${IP_SKIP}"| awk -F"${IP_SKIP}" '{print $2}')
echo my IP: $IP 
RESP=$(curl -s "${UP_SERVER}?type=${UP_TYPE}&sig=${PASSWORD}&type=${UP_TYPE}&ip=${IP}&rand=0")
echo "$RESP"