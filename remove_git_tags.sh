#!/bin/bash

# This script removes unwanted tags

for i in $(git branch -l)
do
	if [ $i != "master" ]
	then
		if [ $i != "release" ]
		then
					git push -d origin $i
				fi
			fi
done




