#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export EXP=data-prep

export EXP_MODEL_PREFIX=$EXP-sm
export EXP_PIECE_PREFIX=spm
export DATA_DIR=~/experiments/twee/nmt-exp/$EXP

export EXP_SRC=qu
export EXP_TRG=re

export TRAIN_PREFIX=train
export TUNE_PREFIX=tune.clean
export DEVEL_PREFIX=devel
export EVAL_PREFIX=eval

export EXP_TRAIN_SRC=$DATA_DIR/$TRAIN_PREFIX.$EXP_PIECE_PREFIX.$EXP_SRC
export EXP_TRAIN_TRG=$DATA_DIR/$TRAIN_PREFIX.$EXP_PIECE_PREFIX.$EXP_TRG
export EXP_TUNE_SRC=$DATA_DIR/$TUNE_PREFIX.$EXP_PIECE_PREFIX.$EXP_SRC
export EXP_TUNE_TRG=$DATA_DIR/$TUNE_PREFIX.$EXP_PIECE_PREFIX.$EXP_TRG
export EXP_VALID_SRC=$DATA_DIR/$DEVEL_PREFIX.$EXP_PIECE_PREFIX.$EXP_SRC
export EXP_VALID_TRG=$DATA_DIR/$DEVEL_PREFIX.$EXP_PIECE_PREFIX.$EXP_TRG
export EXP_EVAL_SRC=$DATA_DIR/$EVAL_PREFIX.$EXP_PIECE_PREFIX.$EXP_SRC
export EXP_EVAL_TRG=$DATA_DIR/$EVAL_PREFIX.$EXP_PIECE_PREFIX.$EXP_TRG

export EXP_DICT_SRC=$DATA_DIR/shared-vocab.$EXP_SRC$EXP_TRG.json
export EXP_DICT_TRG=$DATA_DIR/shared-vocab.$EXP_SRC$EXP_TRG.json
export EXP_PIECE_MODEL=$DATA_DIR/$EXP_SRC$EXP_TRG.model
export EXP_MOSES_SCRIPTS_DIR=/home/matiss/tools/mosesdecoder/scripts

export EXP_PROCESS_VALID_TRG=$DATA_DIR/$DEVEL_PREFIX.rr.lc.$EXP_TRG
export EXP_PROCESS_EVAL_TRG=$DATA_DIR/$EVAL_PREFIX.rr.lc.$EXP_TRG


export EXP_MODEL_DIR=models-$EXP_MODEL_PREFIX-$EXP_SRC-$EXP_TRG

mkdir -p $DIR/$EXP_MODEL_DIR


export GPU_ID="0 1"