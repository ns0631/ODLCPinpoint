import os

path = './data/'

folders = ['train/', 'valid/', 'test/']
sub_directories = ['images/', 'labels/']

count = 0
for folder in folders:
    os.mkdir(path + folder)
    for dir in sub_directories:
        os.mkdir(path + folder + dir)
