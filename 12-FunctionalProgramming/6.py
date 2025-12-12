#Enter distance in km: 70
#Enter number of travel hours: 1
#Enter number of travel minutes: 23
#Average speed: 50.6 km/h 

distance=int(input('Distance: '))
travel_time_hour=int(input('Travel time hour: '))
travel_time_minutes=int(input('Travel time minutes: '))

avg_speed = lambda a,b,c : a/(b+(c/60))

result= avg_speed(distance,travel_time_hour,travel_time_minutes)
print(result)