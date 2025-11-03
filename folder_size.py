import os

my_folder = 'data'

# Given the folder above please sum up the space occupied by all files and folders inside it.

os.listdir(my_folder) # List files/folders inside a folder

os.path.isdir(my_folder) # Check if it is a folder
#os.path.isfile(my_file)  # Check if it is a regular file
fold_size = os.path.getsize(my_folder) # Get the size of a file
#print(fold_size)

#print(os.path.getsize(my_folder))


def space_occupied(my_file):
    if os.path.isfile(my_file):
        return os.path.getsize(my_file)
    if os.path.isdir(my_file):
        space_count = 0
        for f in os.listdir(my_file):
            space_count += space_occupied(os.path.join(my_file, f))
        return space_count

print(space_occupied(my_folder))