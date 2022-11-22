#!/bin/bash

FOLDER=$1

if [ -f $FOLDER ]; then
   echo "$FOLDER exists"
else
   mkdir -p $FOLDER
fi