#!/bin/bash

MOSES_SCRIPTS=~/tools/mosesdecoder/scripts

cat | \
./usr-url.sh | \
./usr-url-start-end.sh | \
./emotikons.sh | \
./emoji.perl | \
$MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | \
$MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv | \
sed 's/@ USR/@USR/g' | \
sed 's/@ URL/@URL/g'