import tensorflow as tf
from tensorflow.models.rnn import rnn


def read_genome(file):
    """
    """
    with tf.gfile.GFile(file, "r") as f:
        return "".join(f.read().split())

file_path = "data/ucsc.hg19.fasta"

#read_genome(file_path)

class Config(object):
    batch_size = 256
    learning_rate = 0.1

config = Config()
print(config.batch_size)


