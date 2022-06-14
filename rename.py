import os
from glob import glob

dir_ = glob('Kaggleface\\face\\*')
# print(dir_)

for i in dir_:
    sub = glob('{}\\*.png'.format(i))
    
    for j in sub:
        age = int(j.split('\\')[-2])
        name = j.split('\\')[-1]
        out_name = 'Kaggleface\\face\\{}_{}'.format(age, name)
        os.rename(j, out_name)