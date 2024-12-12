import pandas as pd
import argparse
import csv

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('csvpaths', nargs='+', help='Absolute path to input CSV')
    parser.add_argument('outdir', help='Absolute path to output directory')
    return parser.parse_args()

def read(paths):
    dfs = []
    for path in paths:
        dfs.append(pd.read_csv(path))
    return dfs

def concat(dfs):
    return pd.concat(dfs)

def write(df, output_directory):
    df.to_csv(f'{output_directory}/CSVConcat.csv', index=False, quoting=csv.QUOTE_ALL)

def main():
    try:
        args = init()
        print('Concatenating...')
        result = concat(read(args.csvpaths))
        print('Writing to output directory...')
        write(result, args.outdir)
        print('Done')
    except FileNotFoundError:
        print('Cannot find one or more of the input files')
    except FileExistsError:
        print('Cannot write to a file that already exists')
    except PermissionError:
        print(f'You either do not have permission to read from input directories or write to output directory')
    except:
        print('An error occurred')

if __name__ == '__main__':
    main()        
