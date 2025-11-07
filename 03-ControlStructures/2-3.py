###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E): ').upper()
distance = int(input('Enter distance in km: '))
fuel_spent=0

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption=9  
elif driving_mode =='E':
    fuel_consumption=6
else:
    print("No driving mode selected")
    exit()

fuel_spent=distance*fuel_consumption/100

total_consumption = ...
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {fuel_spent} liters')