import os
from PIL import Image

directory = './monster_img'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        # creating a object
        image = Image.open(f).convert('RGB')
        MAX_SIZE = (100, 100)
        image.thumbnail(MAX_SIZE)
        # creating thumbnail
        image.save(f)
