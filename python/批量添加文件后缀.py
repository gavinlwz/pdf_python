# import os
#
# path = 'D:\Desktop\少女印画 123'
# file_names = os.listdir(path)
#
# for temp in file_names:
#     img = os.path.join(path, temp)
#     fname, ext = os.path.splitext(img)
#     base_name = os.path.basename(fname)
#     new_n = base_name + '.zip' + ext
#
#     print(os.path.join(path, new_n))
#     os.rename(os.path.join(path, temp), os.path.join(path, new_n))


# -*- coding: utf-8 -*-
import os
import zipfile

path = 'D:\Desktop\少女印画 123'
L = []
for root, dirs, files in os.walk(path):
    for file in files:
        L.append(file)
    for i in L:
        zip = zipfile.ZipFile(path + i, 'w')
        zip.extractall(path='D:\Desktop\少女印画 123')
        zip.close()
print('ok')
