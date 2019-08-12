from __future__ import print_function

import os
import time
import numpy as np
import tensorflow as tf
import pandas as pd
from collections import defaultdict

from sklearn.metrics import roc_auc_score, accuracy_score
import nltk

from correct_text import train, decode, decode_sentence, evaluate_accuracy, create_model, get_corrective_tokens, DefaultPTBConfig, DefaultMovieDialogConfig
from text_corrector_data_readers import PTBDataReader, MovieDialogReader

root_data_path = "data/cornell-movie-dialogs-corpus"
train_path = os.path.join(root_data_path, "processed_movie_lines.txt")
val_path = os.path.join(root_data_path, "processed_movie_lines.txt")
test_path = os.path.join(root_data_path, "processed_movie_lines.txt")
model_path = os.path.join(root_data_path, "dialog_correcter_model_testnltk")
config = DefaultMovieDialogConfig()

data_reader = MovieDialogReader(config, train_path)

train(data_reader, train_path, val_path, model_path)