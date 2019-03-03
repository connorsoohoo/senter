import pandas as pd
import json
import argparse
from datetime import datetime

def write_as_dict(input_name, output_name, size_limit):
    data = []
    df = pd.read_csv(input_name, header=0, sep=',', index_col=None)
    timestamps = df[6].toList()
    sentiment = df[7].toList()

    limit = len(timestamps) if size_limit < 0 else size_limit

    for i in range(limit):
        dt_obj = datetime.strptime(timestamps[i], '%m/%d/2019 %H:%M:%S')
        start_time = datetime(2019, 1, 1)
        time_since = (dt_obj - start_time).total_seconds()
        data.append({'x': time_since, 'val_0': sentiment[i]})

    with open(output_name, 'w') as file:
        file.write(json.dumps(data))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", action="store", dest="input_file", type=str, required=True)
    parser.add_argument("-o", "--output", action="store", dest="output_file", type=str, required=True)
    parser.add_argument("-l", "--size-limit", action="store", dest="size_limit", type=int, default=-1)
    args = parser.parse_args()

    write_as_dict(args.input_name, args.output_name, args.size_limit)
