#! /usr/bin/env python3
"""
readers.py
Utilities for reading lists and such from simple text files
"""

import os
import sys

from collections import OrderedDict

def read_list_file(path, delim = None, expect = None, strict = False, comment = "#"):

	if expect is None:
		expect = 1
	expect = int(expect)
	path = os.path.expandvars(path)
	with open(path, "r") as this_file:

		for line in this_file:
			line = line.strip()
			first = line[0]
			if first in comment:
				continue
			if expect is None:
				maxsplit = -1
			pieces = line.split(sep = delim)
			howmany = len(pieces)
			if not strict:
				rez = []
				for ii in range(0, expect):
					if ii >= howmany:
						rez.append(none)
					else:
						rez.append(pieces[ii])
				if len(rez) == 1:
					yield rez[0]
				else:
					yield rez
			else:
				if expect == 1:
					yield pieces[0]
				else:
					yield pieces[:expect]

def file_prefix(path):

	bname = os.path.basename(path)
	prefix = bname
	while True:
		prefix, suffix = os.path.splitext(prefix)
		if not len(suffix):
			return prefix
