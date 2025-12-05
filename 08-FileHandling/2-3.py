###
# Makes a copy of a text file
#

# file names
original_file = r'08-FileHandling\healthy_lifestyle.txt'
target_file = r'08-FileHandling\copy_healthy_lifestyle.txt'
#content=""
# read the content of the original file
with open(original_file,'r') as file:
    content = file.read()

# write the content to the target file (copy)
with open(target_file,'w') as file:
    file.write(content)
