import re

def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content



file_read=read_from_file(r'08-FileHandling\report.txt')
#file_read.split()

patern=r'€\d+'
sum_of=0
temp=re.findall(patern,file_read)

print(sum_of)
