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