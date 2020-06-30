#!/bin/bash

MOSES_SCRIPTS=~/tools/mosesdecoder/scripts
TRAIN=full.tok
DEV=devel
EVA=eval

#Tekstvienībās sadalīti novērtēšanas un pielāgošanas korpusi bez citām izmaiņām
cat $DEV.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.tok.qu
cat $DEV.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.tok.re
cat $EVA.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.tok.qu
cat $EVA.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.tok.re

# + ar aizstātiem USR un URL
./usr-url.sh < $DEV.qu > $DEV.uu.qu
./usr-url.sh < $DEV.re > $DEV.uu.re
./usr-url.sh < $EVA.qu > $EVA.uu.qu
./usr-url.sh < $EVA.re > $EVA.uu.re
cat $DEV.uu.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.uu.tok.qu
cat $DEV.uu.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.uu.tok.re
cat $EVA.uu.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.uu.tok.qu
cat $EVA.uu.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.uu.tok.re

# + bez USR un URL sākumā/beigās
cat $DEV.uu.qu | ./usr-url-start-end.sh | ./usr-url-start-end.sh > $DEV.uuse.qu
cat $DEV.uu.re | ./usr-url-start-end.sh | ./usr-url-start-end.sh > $DEV.uuse.re
cat $EVA.uu.qu | ./usr-url-start-end.sh | ./usr-url-start-end.sh > $EVA.uuse.qu
cat $EVA.uu.re | ./usr-url-start-end.sh | ./usr-url-start-end.sh > $EVA.uuse.re
cat $DEV.uuse.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.uuse.tok.qu
cat $DEV.uuse.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.uuse.tok.re
cat $EVA.uuse.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.uuse.tok.qu
cat $EVA.uuse.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.uuse.tok.re

# + bez USR un URL sākumā/beigās
./emotikons.sh < $DEV.uuse.qu > $DEV.uusee.qu
./emotikons.sh < $DEV.uuse.re > $DEV.uusee.re
./emotikons.sh < $EVA.uuse.qu > $EVA.uusee.qu
./emotikons.sh < $EVA.uuse.re > $EVA.uusee.re
cat $DEV.uusee.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.uusee.tok.qu
cat $DEV.uusee.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $DEV.uusee.tok.re
cat $EVA.uusee.qu | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.uusee.tok.qu
cat $EVA.uusee.re | $MOSES_SCRIPTS/tokenizer/normalize-punctuation.perl -l lv | $MOSES_SCRIPTS/tokenizer/tokenizer.perl -l lv > $EVA.uusee.tok.re

# Visus vienā
cat $DEV.tok.qu $DEV.uu.tok.qu $DEV.uuse.tok.qu $DEV.uusee.tok.qu > $DEV.all.tok.qu
cat $DEV.tok.re $DEV.uu.tok.re $DEV.uuse.tok.re $DEV.uusee.tok.re > $DEV.all.tok.re
cat $EVA.tok.qu $EVA.uu.tok.qu $EVA.uuse.tok.qu $EVA.uusee.tok.qu > $EVA.all.tok.qu
cat $EVA.tok.re $EVA.uu.tok.re $EVA.uuse.tok.re $EVA.uusee.tok.re > $EVA.all.tok.re

# Un prom!
# Remove development and evaluation data from training data
# This tool is not included - ask https://github.com/pmarcis
mono ~/tools/mp-tools/FilterTestDataFromTrainingData2.exe -P $DEV.all.tok.qu $DEV.all.tok.re $EVA.all.tok.qu $EVA.all.tok.re $TRAIN.qu $TRAIN.re $TRAIN.clean.qu $TRAIN.clean.re

python empty.py devel.uusee.tok.qu devel.uusee.tok.re
python empty.py eval.uusee.tok.qu eval.uusee.tok.re
