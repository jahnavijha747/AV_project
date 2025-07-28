import pandas as pd 

input_file = "flight_sample_2022-09-03.csv.gz"

print("Loading data...")
df = pd.read_csv(input_file, compression="gzip")

print(f"Original shape: {df.shape}")

print("Columns in file:")
print(df.columns)

df_small = df.sample(n=1000, random_state=42) 

colums_to_keep = ['FL_DATE', 'OP_CARRIER', 'ORIGIN', 'DEST', 'DEP_TIME', 'ARR_TIME'] 

print(f"Reduced shape: {df_small.shape}")

output_file = "flight_sample_SMALL.csv"
df_small.to_csv(output_file, index=False)

print(f"Saved reduced file as: {output_file}")
