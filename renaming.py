import os
import glob

path = './photos/'
files = glob.glob(path + "*")

for i, f in enumerate(files):
    name = "Saitama_" + "{0:03d}.jpg".format(i+1)
    os.rename(f, path + name)
    print(f + " → " + name)

print('rename completed')