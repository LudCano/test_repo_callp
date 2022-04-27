#!/bin/bash

start=`date +%s.%N`
cat *.txt >> all.txt
end=`date +%s.%N`

runtime=$( echo "$end - $start" | bc -l )
echo "$runtime"