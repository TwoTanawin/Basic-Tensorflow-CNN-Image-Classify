import os

folder_path = '/Users/twomac/Documents/Two/AI-Center/Classifier/Classifier/myClassify/maskDataset/test/with_mask'
file_prefix = 'img'

file_list = os.listdir(folder_path)
file_list.sort()  # Sort the file list in alphabetical order

for index, filename in enumerate(file_list):
    file_ext = os.path.splitext(filename)[1]  # Get the file extension
    new_filename = f'{file_prefix}{index+1:03d}{file_ext}'  # Generate the new filename with leading zeros
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
