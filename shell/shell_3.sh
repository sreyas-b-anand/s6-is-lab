#!/bin/bash

read -p "Enter filename to remove execute permission: " file

if [ -f "$file" ]; then
    chmod a-x "$file"
    echo "Execute permission removed from $file"
else
    echo "File not found!"
fi