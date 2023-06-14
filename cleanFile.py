import os

folder_path = 'myClassify/maskDataset/test/'

file_path = os.path.join(folder_path, '.DS_Store')

if os.path.exists(file_path):
    os.remove(file_path)
