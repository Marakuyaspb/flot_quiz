import os

directory = '/home/a/flot/static/img/gallery/modern'
output_file = '/home/a/flot/static/img/gallery/modern/names.txt'

# Get all file names in the directory
file_names = [f for f in os.listdir(directory) if f.endswith('.jpg')]

# Write the file names to the output file
with open(output_file, 'w') as file:
    for name in file_names:
        file.write(name.replace('.jpg', '') + '\n')

print('I did it! Look here, madam:', output_file)