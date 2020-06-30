#!/bin/bash

MOSES_SCRIPTS=~/tools/mosesdecoder/scripts
PREFIX=init.train

cat init.train.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > init.train.tok.qu
cat init.train.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > init.train.tok.re

# Split dataset into training, development and evaluation data
# This tool is not included - ask https://github.com/pmarcis
mono ~/tools/mp-tools/GetDevAndTestSetFromCorpus.exe $PREFIX qu re 500 1000

mv $PREFIX.dev.qu devel.qu
mv $PREFIX.dev.re devel.re
mv $PREFIX.eval.qu eval.qu
mv $PREFIX.eval.re eval.re


cat *.train.tok.qu > full.tok.qu
cat *.train.tok.re > full.tok.re


$MOSES_SCRIPTS/training/clean-corpus-n.perl full.tok qu re full.c.tok 1 128

