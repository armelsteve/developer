#!/bin/bash

host=$hostname
user=$username
password=$password

#checking if the repo was updated or not

script=`git status -uno | grep -i "nothing to commit" | awk '{print $1 " "  $2 " " $3}'`

if [[ $script == "nothing to commit" ]]
then
    echo "There is nothing to do"
    exit 0
fi

#checking if the files have been changed or modified

sshpass -p $password ssh -t -oStrictHostKeyChecking=no user@host << EOF
    #command to execute 

    ls -la /Users/tamegj01/.jenkins/config-1.3.1.jar 
    /Users/tamegj01/.jenkins/ojdbc7.jar
EOF