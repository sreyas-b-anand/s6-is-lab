#!/bin/bash

echo "Enter username : "
read user

while true
do
    if who | grep -qw "$user"
	then
        	echo "User $user has logged in!"
        break
    else
        echo "User not logged in. Checking again in 30 seconds..."
        sleep 30
    fi
done
