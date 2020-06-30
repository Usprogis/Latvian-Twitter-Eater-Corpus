#!/bin/bash

#Remove some emotikons
cat | \
sed -E 's/:p+//g' | \
sed -E 's/:P+//g' | \
sed -E 's/:d+//g' | \
sed -E 's/:D+//g' | \
sed -E 's/;d+//g' | \
sed -E 's/;D+//g' | \
sed -E 's/:\)+//g' | \
sed -E 's/;\)+//g' | \
sed -E 's/:-\)+//g' | \
sed -E 's/:\/+//g'