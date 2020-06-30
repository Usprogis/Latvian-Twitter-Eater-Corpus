#!/bin/bash

#Remove URL and USR at the beginning and the end
cat | \
sed ':a;N;$!ba;s/\n@USR /\n/g' | \
sed ':a;N;$!ba;s/\n@URL /\n/g' | \
sed ':a;N;$!ba;s/@USR\n/\n/g' | \
sed ':a;N;$!ba;s/@URL\n/\n/g' | \
sed ':a;N;$!ba;s/@URL via \n/\n/g' | \
sed ':a;N;$!ba;s/@URL …\n/\n/g' | \
sed ':a;N;$!ba;s/@URL …pic[^[:space:]]\+\n/\n/g'