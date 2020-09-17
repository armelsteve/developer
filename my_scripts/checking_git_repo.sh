#!/bin/bash

user=$username
password=$password
url=$bitbucket_url

#checking if the repo was updated or not

script=`git status -uno | grep -i "nothing to commit" | awk '{print $1 " "  $2 " " $3}'`

if [[ $script == "nothing to commit" ]]
then
    echo "There is nothing to do"
    exit 0  
fi

path=`echo $(basename "$url" ".${url##*.}")`

a=`echo $url | cut -d '/' -f3`
b=`echo $url | cut -d '/' -f4`
c=`echo $url | cut -d '/' -f5`
d=`echo $url | cut -d '/' -f6`

var=`echo $a/$b/$c/$d`

echo $path

echo $var

mkdir $path

sleep 2

cd ./$path

git clone https://$user:$password@$var

check_change=`git status -uno | grep -i "nothing to commit" | awk '{print $1 " "  $2 " " $3}'`

if [[ $check_change == "nothing to commit" ]]
then
    echo "There is nothing to do"
    exit 0
else:
    echo "Build in the next stage"
    
fi
