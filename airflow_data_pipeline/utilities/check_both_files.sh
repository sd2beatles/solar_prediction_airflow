#!/bin/bash

FILE1=$1 
FILE2=$2

if [[ -f $FILE1 &&  -f $FILE2 ]]; then
   echo "File $FILE1 and $FILE2 exists"
else
   echo "One or more is missing"
fi
