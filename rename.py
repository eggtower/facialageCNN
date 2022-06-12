import os
from glob import glob

dir_ = glob('Kaggleface/face/*')
print(dir_)

for i in dir_[:10]:
    sub = glob('{}/*.png')
    print(sub)