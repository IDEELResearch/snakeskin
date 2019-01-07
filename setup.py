#! /usr/bin/env python3

from setuptools import setup

setup(
	name = "snakeskin",
	version = "0.1.0",
	description = "some Python utilities to facilitate writing Snakemake pipelines",
	url = "http://github.com/IDEELResearch/snakeskin",
	author = "Andrew Parker Morgan",
	author_email='andrew.parker.morgan@gmail.com',
	license= "MIT",
	packages = ["snakeskin"],
	# scripts=["bin/snakeit"],
	install_requires = [
		"snakemake",
		"yaml"
	],
	zip_safe = False
)
