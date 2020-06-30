#!/bin/bash

cat | \
sed 's/@[^[:space:]]\+/@USR/g' | \
sed 's/http[^[:space:]]\+/@URL/g' | \
sed 's/@URL @URL/@URL/g' | \
sed 's/@URL @URL/@URL/g' | \
sed 's/@USR @USR/@USR/g' | \
sed 's/@USR @USR/@USR/g' | \
sed 's/@USR @USR/@USR/g' | \
sed 's/@USR @USR/@USR/g' | \
sed 's/@USR @USR/@USR/g' | \
sed 's/@USR @USR/@USR/g'