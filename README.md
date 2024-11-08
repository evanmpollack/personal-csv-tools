# Personal CSV Tools

## Overview
A collection of quick and dirty csv tools to automate common tasks. Each were written in about 30 min and are rough around the edges but get the job done.

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

```
python extractcsv.py csvpath outdir [fields...]
```
- csvpath: absolute path to source csv
- outdir: absolute path to output directory
- fields: column names to extract, separated by space