import os
import shutil


baseDir = "/home/chun/Documents/FYP/Data_Subset"
dest1 = '/home/chun/Documents/FYP/Data_Subset2'

dir = os.listdir(baseDir)
for x in range(len(dir)):
    newDir = baseDir + '/' + dir[x]
    dir2 = os.listdir(newDir)
    for y in range(len(dir2)):
        newDir2 = newDir + '/' + dir2[y]
        print(newDir2)
        dir3 = os.listdir(newDir2)
        for z in range(len(dir3)):
            newDir3 = newDir2 + '/' + dir3[z] + "/"
            print(newDir3)
            dir4 = os.listdir(newDir3)
            for f in dir4:
                    shutil.move(newDir3 + f, dest1)



