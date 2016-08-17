
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import h5py
import logging
import numpy as np
import sklearn

class Reader(object):
    """ Reader for fasta sequence to provide batch data
    """
    def __init__(self, data_path, batch_size):
        self._data_path = data_path
        fasta_name = "ucsc.hg19.fasta"
        fai_name = fasta_name + ".fai"
        self._fasta = fasta_name
        self._fai = fasta_name + ".fai"
        self.batch_size = batch_size
        self.contig = contig
        self.raw_h5 = fasta_name + ".h5"
        
        if not os.path.exits(fasta_name):
            _download_fasta()
        if not os.path.exits(fai_name):
            _build_fai()
        if not os.path.exits(self.raw_h5):
            _build_raw_h5()

    def _build_raw_h5(self):
        """build raw hdf5 file from fasta
        """
        logging.info("building raw hdf5 ")
        with h5open(self.raw_h5,"w") as h5:
            contig = ""
            seq = []
            i = 0
            for line in self.fasta:
                i += 1
                if i % 1000000 == 0:
                    logging.warn("process")
                if !line.startswith(">chr"):
                    seq.append(chomp(line))
                else:
                    if len(seq) > 0:
                        h5write(h5, contig, "".join(seq))
                    contig = chomp(line)
                    seq = []


    def _raw_data(self, contig):
        """ Load raw fasta data from raw_h5 hdf5 file
        Args:
          contig: chromesome name
        Returns:
          (train_data,valid_data,test_data,vocabulary)
        """
        pass


    def iterator(self, contig, batch_size, num_steps):
        pass
    



def _fastaTocontig(self):
    for line in self.fasta:
        pass

def _download_fasta():
    pass
    
def _build_fai():
    pass

    
