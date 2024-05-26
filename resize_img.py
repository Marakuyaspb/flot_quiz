import os
import PIL
from PIL import Image

dir_path = '/home/a/flot/static/img/gallery/modern/trumb'

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = Image.open(os.path.join(dir_path, filename))

        width, height = img.size
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        resized_img = img.resize((new_width, new_height))
        resized_img.save(os.path.join(dir_path, 'resized_' + filename))
print('I did it, madam! ')