#!/bin/bash

IP_SERVER="[yourhost]/me"
IP_SKIP="Address: "
PASSWORD="password"
UP_SERVER="[yourhost]/up"
UP_TYPE="home"


IP=$(curl -s "${IP_SERVER}" | grep "${IP_SKIP}"| awk -F"${IP_SKIP}" '{print $2}')
echo my IP: $IP 
RESP=$(curl -s "${UP_SERVER}?type=${UP_TYPE}&sig=${PASSWORD}&type=${UP_TYPE}&ip=${IP}&rand=0")
echo "$RESP"
