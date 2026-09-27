#!/bin/bash

FILE_TO_CHECK="$1"

if [ -z "$FILE_TO_CHECK" ]; then
    echo "Usage: $0 <file>"
    exit 2
fi

if [ -f "$FILE_TO_CHECK" ]; then
    echo "The file exists: $FILE_TO_CHECK"
    exit 0
else
    echo "The file does not exist: $FILE_TO_CHECK"
    exit 1
fi
