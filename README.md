# snakeskin

A Python module to house utility functions to facilitate writing genomics-oriented Snakemake pipelines.

## Example usage
```
from snakeskin import readers, configs, formats

# read pairs of items from a text file
iid, group = readers.read_list_file("file.txt", expect = 2)

# augment `config` object auto-created by Snakemake with defaults in another file
config = configs.impute_defaults(config, "alt_config.yaml")

# same as above, but with manually-created dict of options
config = configs.impute_defaults(config, { "threads": 4 })

# same as above, but looks for "defaults.yaml" in working directory if no defaults specified
config = configs.impute_defaults(config)

# strip leading directories and trailing extension(s) from a file name
what_genome = readers.file_prefix("/path/to/genomes/pf_3d7.fa")

# read chromosome sizes for a reference genome
chroms = formats.read_chrom_sizes("pf_3d7.fa")

# auto-generate name of index file from file extension
fai = formats.guess_index_name("pf_3d7.fa")

# check if index file is present, auto-guessing index from file extension
is_indexed = formats.has_index("pf_3d7.fa")
```

The package provides a wrapper script called `snakeit` that does a man-in-the-middle on Snakemake job-scripts and submits them to the Slurm scheduler, capturing memory requirement, threads, etc from job parameters and using sensible defaults if such parameters are not present.

```
snakemake \
	--snakefile pipeline.snake \
	--config config.yaml \
	--cluster snakeit
```
