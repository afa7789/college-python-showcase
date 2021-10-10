#!/bin/bash

for i in $(ls); do
	if [ -d $i ];then
		cd $i 	
		echo removing git from $i
		rm -rf .git
		cd ..
	fi
done;
