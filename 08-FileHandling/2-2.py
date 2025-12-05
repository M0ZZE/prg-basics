seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]


# Name of the file to write to
file_name = r'08-FileHandling\seven_wonders.txt'

# Sort data alphabetically
...

# Write data to the file
with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(f'{item}\n')