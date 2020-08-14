#No.3
#3.1
bicycles = ['trek', 'cannonable', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#3.2
bicycles[0] = 'ducati'
print(bicycles[0])
print(bicycles)

bicycles.append('yamaha')
print(bicycles)

bicycles.insert(4, 'suzuki')
print(bicycles)

del bicycles[5]
print(bicycles)

popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

popped_bicycle = bicycles.pop(1)
print(bicycles)
print(popped_bicycle)

bicycles.remove('ducati')
print(bicycles)

too_expensive = 'redline'
bicycles.remove(too_expensive)
print(bicycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#3.3
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.reverse()
print(cars)

print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the resorted list:")
print(sorted(cars, reverse=True))
print("Here is the original list again:")
print(cars)
print(len(cars))

#No.4
#4.1
for car in cars:
    print(car)
    print(car.title() + ", that was a great car!")
    print("I can't wait to see your new car, " + car.title() + ".\n")

numbers = list(range(1, 6))
print(numbers)
#4.2
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
sum(squares)
#4.3
squares = [value**2 for value in range(1, 11)]
print(squares)
#4.4
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[:3])
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
your_players = players[:]
print(players)
print(your_players)
your_players.append('marvin')
print(your_players)
print(players)
#4.5
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)

#5.4
requested_toppings = ['mushrooms', 'green peppers', 'french fries']
#requested_toppings = []
available_toppings = ['mushrooms', 'olives', 'green peppers',
'prpperono', 'pineapple', 'extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            if requested_topping == 'green peppers':
                print("Sorry, we are out of green peppers right now.")
            else:
                print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#No.6
#6.1
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
#6.2
alien_0['speed'] = 'medium'
print("The original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position'])) 