import pandas as pd
import os

input_folder = "./"
output_folder = "./shrinked/"
os.makedirs(output_folder, exist_ok=True)

files_to_shrink = [
    "flight_sample_2022-09-01.csv.gz",
    "flight_sample_2022-09-03.csv.gz",
    "flight_sample_2022-09-02.csv.gz",
    "states.csv"
]

for filename in files_to_shrink:
    input_file = os.path.join(input_folder, filename)
    print(f"Processing {filename}...")

    # Check if file is gzipped or not
    if filename.endswith('.gz'):
        df = pd.read_csv(input_file, compression='gzip')
    else:
        df = pd.read_csv(input_file)  # no compression

    df_small = df.sample(frac=0.1)
    output_file = os.path.join(output_folder, f"small_{filename.replace('.gz','')}")
    df_small.to_csv(output_file, index=False)

    print(f"Saved smaller file as {output_file}")

