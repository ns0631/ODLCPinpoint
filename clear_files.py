import os

path = './dataset/'

folders = ['train/', 'valid/', 'test/']
sub_directories = ['images/', 'labels/']

count = 0
for folder in folders:
    for dir in sub_directories:
        fpath = path + folder + dir
        for file in os.listdir(fpath):
            os.remove(fpath + file)
            count += 1
print(f'Cleared {count} files.')
