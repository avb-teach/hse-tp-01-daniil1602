#!/usr/bin/env bash

max_depth_p=-1
in=$1
out=$2
while [ -n "$1" ]
do
    case "$1" in
    "--max_depth" )
            max_depth_p="$2"
            ;;
    esac
    shift
done
if (( max_depth_p==-1)); then
  python3 main.py $in $out 0
else
    python3 main.py $in $out $max_depth_p
fi


