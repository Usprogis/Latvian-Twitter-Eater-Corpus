#!/bin/bash

MOSES_SCRIPTS=~/tools/mosesdecoder/scripts
TRAINFOOD=full-food-qr
TRAINMP=all-qa-question-tweets
EVA=eval.orig
DEV=devel.orig

#Prepare data
./prepare.sh < $TRAINFOOD.qu > $TRAINFOOD.tok.qu
./prepare.sh < $TRAINFOOD.re > $TRAINFOOD.tok.re
./prepare.sh < $TRAINMP.qu > $TRAINMP.tok.qu
./prepare.sh < $TRAINMP.re > $TRAINMP.tok.re
./prepare.sh < $EVA.qu > eval.tok.qu
./prepare.sh < $EVA.re > eval.tok.re
./prepare.sh < $DEV.qu > devel.tok.qu
./prepare.sh < $DEV.re > devel.tok.re

cat $TRAINFOOD.tok.qu $TRAINMP.tok.qu > train.tok.qu
cat $TRAINFOOD.tok.re $TRAINMP.tok.re > train.tok.re

#Remove empty lines if such exist
python empty.py eval.tok.qu eval.tok.re
python empty.py devel.tok.qu devel.tok.re
python empty.py train.tok.qu train.tok.re


$MOSES_SCRIPTS/training/clean-corpus-n.perl train.tok.ne qu re train.tok.ne.c 1 128

# Remove development and evaluation data from training data
# This tool is not included - ask https://github.com/pmarcis
mono ~/tools/mp-tools/FilterTestDataFromTrainingData2.exe -P \
	devel.tok.ne.qu \
	devel.tok.ne.re \
	eval.tok.ne.qu \
	eval.tok.ne.re \
	train.tok.ne.c.qu \
	train.tok.ne.c.re \
	train.tok.ne.cc.qu \
	train.tok.ne.cc.re

#Lowercase
$MOSES_SCRIPTS/tokenizer/lowercase.perl < train.tok.ne.cc.qu > train.lc.qu &
$MOSES_SCRIPTS/tokenizer/lowercase.perl < train.tok.ne.cc.re > train.lc.re &
$MOSES_SCRIPTS/tokenizer/lowercase.perl < eval.tok.ne.qu > eval.lc.qu &
$MOSES_SCRIPTS/tokenizer/lowercase.perl < eval.tok.ne.re > eval.lc.re &
$MOSES_SCRIPTS/tokenizer/lowercase.perl < devel.tok.ne.qu > devel.lc.qu &
$MOSES_SCRIPTS/tokenizer/lowercase.perl < devel.tok.ne.re > devel.lc.re &

wait

#Remove repetitions
cat train.lc.qu | php repstr.php | php repch.php > train.rr.lc.qu
cat train.lc.re | php repstr.php | php repch.php > train.rr.lc.re
cat eval.lc.qu | php repstr.php | php repch.php > eval.rr.lc.qu
cat eval.lc.re | php repstr.php | php repch.php > eval.rr.lc.re
cat devel.lc.qu | php repstr.php | php repch.php > devel.rr.lc.qu
cat devel.lc.re | php repstr.php | php repch.php > devel.rr.lc.re



cat train.rr.lc.{qu,re} eval.rr.lc.{qu,re} devel.rr.lc.{qu,re} > trains.rr.lc.qure
spm_train --input=trains.rr.lc.qure --model_prefix=qure --vocab_size=8000

spm_encode --model=qure.model < train.rr.lc.qu > train.spm.qu &
spm_encode --model=qure.model < train.rr.lc.re > train.spm.re &

spm_encode --model=qure.model < devel.rr.lc.qu > devel.spm.qu &
spm_encode --model=qure.model < devel.rr.lc.re > devel.spm.re &

spm_encode --model=qure.model < eval.rr.lc.qu > eval.spm.qu &
spm_encode --model=qure.model < eval.rr.lc.re > eval.spm.re &

wait

sed -i 's/▁@ USR/▁@USR/g' train.spm.qu
sed -i 's/▁@ USR/▁@USR/g' train.spm.re
sed -i 's/▁@ USR/▁@USR/g' devel.spm.qu
sed -i 's/▁@ USR/▁@USR/g' devel.spm.re
sed -i 's/▁@ USR/▁@USR/g' eval.spm.qu
sed -i 's/▁@ USR/▁@USR/g' eval.spm.re
sed -i 's/▁@ URL/▁@URL/g' train.spm.qu
sed -i 's/▁@ URL/▁@URL/g' train.spm.re
sed -i 's/▁@ URL/▁@URL/g' devel.spm.qu
sed -i 's/▁@ URL/▁@URL/g' devel.spm.re
sed -i 's/▁@ URL/▁@URL/g' eval.spm.qu
sed -i 's/▁@ URL/▁@URL/g' eval.spm.re

sed -i 's/▁\& quot ;/▁\&quot;/g' train.spm.qu
sed -i 's/▁\& quot ;/▁\&quot;/g' train.spm.re
sed -i 's/▁\& quot ;/▁\&quot;/g' devel.spm.qu
sed -i 's/▁\& quot ;/▁\&quot;/g' devel.spm.re
sed -i 's/▁\& quot ;/▁\&quot;/g' eval.spm.qu
sed -i 's/▁\& quot ;/▁\&quot;/g' eval.spm.re

sed -i 's/▁\& apos ;/▁\&apos;/g' train.spm.qu
sed -i 's/▁\& apos ;/▁\&apos;/g' train.spm.re
sed -i 's/▁\& apos ;/▁\&apos;/g' devel.spm.qu
sed -i 's/▁\& apos ;/▁\&apos;/g' devel.spm.re
sed -i 's/▁\& apos ;/▁\&apos;/g' eval.spm.qu
sed -i 's/▁\& apos ;/▁\&apos;/g' eval.spm.re

sed -i 's/▁\& amp ;/▁\&amp;/g' train.spm.qu
sed -i 's/▁\& amp ;/▁\&amp;/g' train.spm.re
sed -i 's/▁\& amp ;/▁\&amp;/g' devel.spm.qu
sed -i 's/▁\& amp ;/▁\&amp;/g' devel.spm.re
sed -i 's/▁\& amp ;/▁\&amp;/g' eval.spm.qu
sed -i 's/▁\& amp ;/▁\&amp;/g' eval.spm.re

#REALITY CHECK

# Remove development and evaluation data from training data
# This tool is not included - ask https://github.com/pmarcis
mono ~/tools/mp-tools/FilterTestDataFromTrainingData2.exe -P \
	devel.spm.qu \
	devel.spm.re \
	eval.spm.qu \
	eval.spm.re \
	train.spm.qu \
	train.spm.re \
	train.spm.ccc.qu \
	train.spm.ccc.re

sockeye-vocab -i train.spm.qu train.spm.re -o shared-vocab.qure.json

