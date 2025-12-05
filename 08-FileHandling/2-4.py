###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = r'08-FileHandling\it_company.csv'
position_file = r'08-FileHandling\software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file,'r') as source:
    with open(position_file,'w') as target:
        for line in source:
            if job_title in line:
                target.write(line)