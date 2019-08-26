#!/bin/bash
#This script will email us our user, IP and hostname
emailaddress="alecnader@gmail.com"
today=$(date +"%m-%d-%Y")
ip=$(/usr/sbin/ifconfig | grep 'inet 192' |awk '{print $2}')

printf -v content "User:\t%s\nMyHostname:\t%s\nMy IP:\t%s\n" $USER $HOSTNAME $ip
mail -s "IT3038C Linux IP" $emailaddress <<< $content
