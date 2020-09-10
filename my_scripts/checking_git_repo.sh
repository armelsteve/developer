#!/bin/bash


#checking if the repo was updated or not


git status -uno 

if [[ $? == 0 ]]
then
        git add .
        git commit -m "sample"
        git push
        echo "Nothing to do!!!"
fi

#elif [[ $(git rev-parse --abbrev-ref HEAD) ]]
#echo "You are in the $(git rev-parse --abbrev-ref HEAD) branch"


