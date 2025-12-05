def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

file_name = r'08-FileHandling\it_company.csv'

file_line=read_from_file(file_name)
file_line=file_line.splitlines()

# Position
job_title = 'Software Engineer'

i=1

#with ... as ...:
for line in file_line:
    if job_title in line:
        print(i,line)
        i+=1