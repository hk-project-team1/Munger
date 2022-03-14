import pandas as pd
import openpyxl
import os

filename = []

path = "C:/workspace/Munger/KiwoomAPI/SemiconductorPriceBF"

for (root, directories, files) in os.walk(path):
        for file in files:
                file_path = os.path.join(root,file)
                filename.append(file_path)
                print(filename)

for path in filename:
        name = path.split("\\")[1]
        df = pd.read_excel(f"{path}", engine='openpyxl')
        df = df[['일자', '현재가']]
        df.to_excel(f'{name}')