#!/bin/bash

read -p "Enter filename to monitor: " file

if [ ! -f "$file" ]; then
    echo "File not found!"
    exit 1
fi

hashfile="$file.hash"

if [ ! -f "$hashfile" ]; then
    sha256sum "$file" > "$hashfile"
    echo "Hash created. File is now being monitored."
else
    sha256sum -c "$hashfile"
fi