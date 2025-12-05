def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

# reads the entire file
file_content = read_from_file(r'08-FileHandling\countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()

#file_lines.sort()
# prints the array
for line in sorted(file_lines):
    print(line)