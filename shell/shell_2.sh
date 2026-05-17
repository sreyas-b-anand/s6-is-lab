#!/bin/bash

read -p "Enter username to check: " username

while true; do
    if who | grep -q "^$username\b"; then
        echo "User $username has logged in!"
        break
    else
        echo "User not logged in. Checking again in 30 seconds..."
        sleep 30
    fi
done