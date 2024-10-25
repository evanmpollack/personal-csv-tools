import pandas as pd
import math
import argparse

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv', help='Absolute path to input CSV')
    parser.add_argument('chunks', type=int, help='Number of chunks')
    parser.add_argument('outpath', help='Absolute path to output directory')
    return parser.parse_args()

def read(path):
    return pd.read_csv(path)

def chunk(df, num_chunks):
    num_rows = df.index.size
    print(f'Initial Row Count: {num_rows}')
    rows_per_chunk = math.ceil(num_rows / num_chunks)
    print(f'Expected Row Count Per Chunk: {rows_per_chunk}')
    starting_chunk = 0
    chunks = []
    chunk = 1
    while starting_chunk < num_rows:
        current_range_max = min(starting_chunk + rows_per_chunk, num_rows)
        print(f'Chunk {chunk}: {current_range_max - starting_chunk} rows')
        chunks.append(df.iloc[starting_chunk:current_range_max])
        starting_chunk = current_range_max
        chunk += 1
    return chunks
        
def write(chunks, output_directory):
    try:
        for index, chunk in enumerate(chunks, start=1):
            chunk.to_csv(f'{output_directory}/CSVChunk_{index}.csv', index=False)
    except FileExistsError:
        print('Cannot write to file that already exists')
    except PermissionError:
        print(f'You do not have permission to write to \'{output_directory}\'')
    except:
        print(f'An error occured writing to \'{output_directory}\'')

def main():
    print('Parsing input...')
    args = init()
    print('Chunking...')
    chunks = chunk(read(args.csv), args.chunks)
    print('Writing to output directory...')
    write(chunks, args.outpath)
    print('Finished')

if __name__ == '__main__':
    main()