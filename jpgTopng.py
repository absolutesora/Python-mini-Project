import sys
import os
from PIL import Image

# grab first and second argument

current_folder = sys.argv[1]
new_folder = sys.argv[2]

# # check if new/ exists, if not create
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
else:
    print("Folder already exists")
width = int(input('Enter the Width value: '))
height = int(input('Enter the Height value: '))

# loop through photos
for filename in os.listdir(f'{current_folder}/'):
    img = Image.open(f'{current_folder}/{filename}')
    resize = img.resize((width,height))
    clean_name = os.path.splitext(filename)[0]
    resize.save(f'{new_folder}/{clean_name}.png','png')
    print(f'conversion done for {filename}, Width:{width}, Height:{height}!')
