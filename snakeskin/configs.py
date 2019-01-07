#! /usr/bin/env python3
"""
config.py
Functions for processing configuration options in Snakemake pipelines
"""

import os
import sys
import yaml

def load_defaults(path = "default.yaml"):

	if path is None:
		path = "default.yaml"
	try:
		return yaml.load(open(path, "r"))
	except:
		return {}

def impute_defaults(this_config, defaults = None):

	if isinstance(defaults, dict):
		## assume defaults already loaded
		this_default = default
	else:
		## try to load defaults from file
		this_default = load_defaults(defaults)

	for opt,value in this_default.items():
		if not opt in this_config:
			this_config[opt] = value

	return this_config
