print("Welcome to python delivery calculator.")
trips = int(input("Enter the number of delivery trip you had made today: "))
total = 0


for i in range(1, trips+1):
    per_trip = int(input("Enter the earnings made for trip" + str(i) + ":"))
    total = total + per_trip
    average = total/trips
print("You have made", trips, "and earned a total of $", total, "with average earning per trip of $", average)
