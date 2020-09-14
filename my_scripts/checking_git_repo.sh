#!/bin/bash


#checking if the repo was updated or not

script=`git status -uno | grep -i "nothing to commit" | awk '{print $1 " "  $2 " " $3}'`

if [[ $script == "nothing to commit" ]]
then
    echo "There is nothing to do"
    exit 0
fi

