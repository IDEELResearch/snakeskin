#! /usr/bin/env python3
"""
formats.py
Simple tools for guessing and manipulating common genomics file formats.
"""

import os
import sys
from re import search as re_search

INDEX_PAIRS = {
	"vcf.gz": "tbi",
	"bam": "bai",
	"cram": "csi",
	"fa": "fai",
	"fna": "fai",
	"fasta": "fai"
}

def guess_index_name(path):

	for ext, idx in INDEX_PAIRS.items():
		ext = ext + "$"
		if re_search(ext, path):
			return path + "." + idx

	return None

def has_index(path, index = None):

	if not index:
		index = guess_index_name(path)
	return os.path.isfile(index)

def read_chrom_sizes(fasta):

	fai = os.path.expandvars(fasta) + ".fai"
	sizes = OrderedDict()
	with open(fai, "r") as fai_file:
		for line in fai_file:
			chrom, size = line.strip().split()[:2]
			sizes[chrom] = size

	return sizes
