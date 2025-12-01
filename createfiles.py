import os
from pathlib import Path 
Root_folder="Zuba"

files_list=[
     f"{Root_folder}/__init__.py",
    f"{Root_folder}/DataPreprocessing/__init__.py",
    f"{Root_folder}/DataPreprocessing/process.py",
    f"{Root_folder}/Model_training/__init__.py",
    f"{Root_folder}/Model_training/train.py",
     f"{Root_folder}/Model_eval/__init__.py",
    f"{Root_folder}/Model_eval/eval.py",
    f"{Root_folder}/notebooks/__init__.py",
    f"{Root_folder}/utils/__init__.py",
    f"{Root_folder}/logger/__init__.py",
    "requirements.txt"
]
for file_path in files_list:
    filepath=Path(file_path)
    file_dir,filename=os.path.split(filepath)
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        print("create directory {}".format(file_dir))
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            print(f"creating empty file:{filename}")
    else:
        print(f"file with name:{filename} already exists")
