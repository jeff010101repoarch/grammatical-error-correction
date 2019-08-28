from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import os
import numpy as np
import tensorflow as tf
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import embedding_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn_ops
import codecs

from correct_text import train, decode, decode_sentence, evaluate_accuracy, create_model,\
    get_corrective_tokens, DefaultPTBConfig, DefaultMovieDialogConfig
from text_corrector_data_readers import PTBDataReader, MovieDialogReader

import seq2seq
from data_reader import PAD_ID, GO_ID


# linux 环境下下面路径没问题， windows下 下面路径名要加全
root_data_path = "data/cornell-movie-dialogs-corpus"
train_path = os.path.join(root_data_path, "processed_movie_lines.txt")
val_path = os.path.join(root_data_path, "processed_movie_lines.txt")
test_path = os.path.join(root_data_path, "processed_movie_lines.txt")
model_path = os.path.join(root_data_path, "dialog_correcter_model_testnltk")
config = DefaultMovieDialogConfig()

data_reader = MovieDialogReader(config, train_path, dropout_prob=0.25, replacement_prob=0.25, dataset_copies=1)
corrective_tokens = get_corrective_tokens(data_reader, train_path)

import pickle
with open(os.path.join(root_data_path, "corrective_tokens.pickle"), "wb") as f:
    pickle.dump(corrective_tokens, f)


import pickle
with open(os.path.join(root_data_path, "token_to_id.pickle"), "wb") as f:
    pickle.dump(data_reader.token_to_id, f)


sess = tf.InteractiveSession()
model = create_model(sess, True, model_path, config=config)



# 如果想检测句子，改引号里的： 
# 例子： decoded = decode_sentence(sess, model, data_reader, "输入检测的句子", corrective_tokens=corrective_tokens)
print('subtraction of articles (a, an, the):') #缺少冠词a an the的错误
decoded = decode_sentence(sess, model, data_reader, "you must have girlfriend", corrective_tokens=corrective_tokens)
print('subtraction of the second part of a verb contraction (e.g. "ve", "ll", "s", "m")') # 缺少谓语的错误
decoded = decode_sentence(sess, model, data_reader, "the Cardinals did better then the Cubs in the offseason", corrective_tokens=corrective_tokens)
print('replacement of a few common homophones with one of their counterparts (e.g. replacing "their" with "there", "then" with "than"):') #用错词的错误
decoded = decode_sentence(sess, model, data_reader, "there's another gig starting in saudi arabia. i just a walk-on this time though. bit-part.", corrective_tokens=corrective_tokens)