"""Preprocesses Cornell Movie Dialog data."""
import nltk
import tensorflow as tf
import codecs

tf.app.flags.DEFINE_string("raw_data", "", "Raw data path")
tf.app.flags.DEFINE_string("out_file", "", "File to write preprocessed data "
                                           "to.")

FLAGS = tf.app.flags.FLAGS


def main(_):
    with codecs.open(FLAGS.raw_data, "r",encoding= u'utf-8',errors='ignore') as raw_data, \
        codecs.open(FLAGS.out_file, "w",encoding= u'utf-8',errors='ignore') as out:
        for line in raw_data:
            parts = line.split(" +++$+++ ")
            dialog_line = parts[-1]
            s = dialog_line.strip().lower()
            # preprocessed_line = nltk.word_tokenize(s)

            preprocessed_line = " ".join(nltk.word_tokenize(s))
            print(preprocessed_line)
            out.write(preprocessed_line + "\n")

if __name__ == "__main__":
    tf.app.run()