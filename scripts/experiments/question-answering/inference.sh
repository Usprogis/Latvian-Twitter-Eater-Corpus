#/bin/bash
. ./data.sh

python -m sockeye.translate \
--device-ids 0 \
--batch-size 20 \
--models $EXP_MODEL_DIR \
--input $EXP_EVAL_SRC \
--output $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.spm.$EXP_TRG

spm_decode --model=$EXP_PIECE_MODEL < $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.spm.$EXP_TRG > $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.tok.$EXP_TRG
php data-prep/repeat.php < $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.tok.$EXP_TRG > $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.tok.nr.$EXP_TRG
$EXP_MOSES_SCRIPTS_DIR/tokenizer/detokenizer.perl -l lv < $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.tok.nr.$EXP_TRG > $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.tc.$EXP_TRG
$EXP_MOSES_SCRIPTS_DIR/recaser/detruecase.perl < $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.tc.$EXP_TRG > $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.$EXP_TRG

sacrebleu -b -w 2 $EXP_PROCESS_EVAL_TRG < $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.$EXP_TRG | tee $EXP_EVAL_SRC.translated-$EXP_MODEL_PREFIX.$EXP_TRG.bleu
