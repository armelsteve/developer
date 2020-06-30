#!/bin/bash

# This script removes unwanted tags

for i in $(git tag -l)
do
	if [ $i != "1.1.0" ]
	then
		if [ $i != "1.1.1" ]
		then
			if [ $i != "1.2.0" ]
			then
				if [ $i != "sprint4-demo" ]
				then
					git push --delete origin $i
				fi
			fi

		fi

	fi

done


