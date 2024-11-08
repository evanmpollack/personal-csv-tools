import pandas as pd
import argparse

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('csvpath', help='Absolute path to input CSV')
    parser.add_argument('outdir', help='Absolute path to output directory')
    parser.add_argument('fields', nargs='+', help='Fields to extract, separated by space')
    return parser.parse_args()

def read(path):
    return pd.read_csv(path)

def extract(df, fields):
    return df[fields]

def write(df, output_directory, fields):
    df.to_csv(f'{output_directory}/CSVSubset_{"_".join(fields)}.csv', index=False)

def main():
    try:
        args = init()
        print('Extracting...')
        subset = extract(read(args.csvpath), args.fields)
        print('Writing to output directory...')
        write(subset, args.outdir, args.fields)
        print('Done')
    except FileNotFoundError:
        print(f'Cannot find input file {args.csvpath}')
    except FileExistsError:
        print('Cannot write to file that already exists')
    except PermissionError:
        print(f'You either do not have permission to read from \'{args.csvpath}\' or write to \'{args.outdir}\'')
    except KeyError:
        print(f'{",".join(args.fields)} are invalid')
    except:
        print('An error occurred')

if __name__ == '__main__':
    main()
