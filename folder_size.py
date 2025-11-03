import os

my_folder = 'data'

# Given the folder above please sum up the space occupied by all files and folders inside it.

os.listdir(my_folder) # List files/folders inside a folder

os.path.isdir(my_folder) # Check if it is a folder
#os.path.isfile(my_file)  # Check if it is a regular file
#os.path.getsize(my_file) # Get the size of a file

print(os.path.getsize(my_folder))
