#!/bin/bash


#checking if the repo was updated or not


git status

if [[ $? == 0 ]]
then
        echo "Nothing to do!!!"
#elif [[ $(git rev-parse --abbrev-ref HEAD) ]]
#echo "You are in the $(git rev-parse --abbrev-ref HEAD) branch"
fi


