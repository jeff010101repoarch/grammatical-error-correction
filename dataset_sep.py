"""Preprocesses Cornell Movie Dialog data."""
import nltk
import tensorflow as tf
import codecs
import random


raw_data = 'data/cornell-movie-dialogs-corpus/processed_movie_lines.txt'
train_data = 'data/cornell-movie-dialogs-corpus/movie_lines_train.txt'
test_data = 'data/cornell-movie-dialogs-corpus/movie_lines_test.txt'
val_data = 'data/cornell-movie-dialogs-corpus/movie_lines_val.txt'

with codecs.open(raw_data, "r",encoding= u'utf-8',errors='ignore') as raw_data, \
    codecs.open(train_data, "w",encoding= u'utf-8',errors='ignore') as out_train, \
    codecs.open(test_data, "w",encoding= u'utf-8',errors='ignore') as out_test, \
    codecs.open(val_data, "w",encoding= u'utf-8',errors='ignore') as out_val:
    for line in raw_data:
        a = random.randint(1,10)
        print(line)
        if a<8:
            out_train.write(line + "\n")
        else:
            if a<10:
                out_val.write(line + "\n")
            else:
                out_test.write(line + "\n")

