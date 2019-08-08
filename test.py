from __future__ import print_function

import os
import time
import numpy as np
import tensorflow as tf
import pandas as pd
from collections import defaultdict

from sklearn.metrics import roc_auc_score, accuracy_score
import nltk

from correct_text import train, decode, decode_sentence, evaluate_accuracy, create_model,\
    get_corrective_tokens, DefaultPTBConfig, DefaultMovieDialogConfig
from text_correcter_data_readers import PTBDataReader, MovieDialogReader