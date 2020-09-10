#!/bin/bash


#checking if the repo was updated or not

git status -uno

if [[ $? == 0 ]]
then
            git add .
            git commit -m "message"
            git push
fi

echo "You are in $(git rev-parse --abbrev-ref HEAD) branch"




