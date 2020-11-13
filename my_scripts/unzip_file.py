import zipfile
import os

path="/Users/armel.gansop/script/developer/my_scripts"
ext = "zip"

list_path = os.listdir(path)

for i in list_path:
    if i.endswith(ext):
        with zipfile.ZipFile(i, 'r') as zip_ref:
            zip_ref.extractall(path)