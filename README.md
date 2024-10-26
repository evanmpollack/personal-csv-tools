# Chunk CSV

## Overview
A quick and dirty script that splits a source CSV into N chunks and puts the chunks in a directory of choice

## Use
1. Install Python 3.10+
2. Create virtualenv
```
python -m venv /path/to/new/virtual/environment
```
3. Install dependencies
```
pip install -r /path/to/requirements.txt
```
4. Run
```
python splitcsv.py csvpath outdir chunks
```
- csvpath: absolute path to source csv
- outdir: absolute path to output directory
- chunks: the number of chunks