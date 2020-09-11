#!/bin/bash


#checking if the repo was updated or not

script=`git status -uno | grep -i "nothing to commit" | awk '{print $1 " "  $2 " " $3}'`

printf "$script"