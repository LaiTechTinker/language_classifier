import pandas as pd
import os


input_folder="./multilingual_dataset"
output_folder="./converted_dataset"
os.makedirs(output_folder,exist_ok=True)
for filename in os.listdir(input_folder):
    if filename.endswith(".tsv"):
        input_filepath=os.path.join(input_folder,filename)
        output_filepath=os.path.join(output_folder,filename.replace(".tsv",".csv"))
        df=pd.read_csv(input_filepath, sep="\t")
        df.to_csv(output_filepath,index=False)
        print(f"Converted {input_filepath} to {output_filepath}")
print("operation done successfully")
