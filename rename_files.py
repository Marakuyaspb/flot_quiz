import os
directory = '/home/a/flot/static/img/gallery/history'

file_names = [f for f in os.listdir(directory) if f.endswith('.jpg')]

# Dictionary to keep track of counts for each first word
word_counts = {}

for file_name in file_names:
    # Extract the first word before a space
    first_word = file_name.split()[0]

    # Update the count for the first word
    count = word_counts.get(first_word, 0)
    word_counts[first_word] = count + 1

    # Construct the new file name
    new_file_name = f'{first_word}.jpg' if count == 0 else f'{first_word}_{count}.jpg'

    # Rename the file
    os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))
    print(f'Renamed {file_name} to {new_file_name}')

print('Files renamed successfully, madam.')