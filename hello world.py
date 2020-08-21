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
favorite_languages = {
    'jen': 'python',
    'sarah': 'ruby',
    'edward': 'c',
    'phil': 'python',
    }
print("Sarah's favorite language is "+
    favorite_languages['sarah'].title() +
    ".")
#6.2
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
#键值对
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
freinds = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in freinds:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#6.3
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
    #print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points' : 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("The total number of aliens: " +
    str(len(aliens)))
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'melium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")
#6.4
pizza = {
    'crust': 'thick',
    'toppings': ['musrooms', 'extra cheese'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())
users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + user_info['last']
    location = user_info['location']
    print("\tFullname is " + full_name.title())
    print("\tLocation is " + location.title())
#No.7
#7.1
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
'''
'''
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("\nYou're a adult now! ")
else:
    print("\nYou're still a child! ")
'''
'''
number = input("\nEnter a number, and I will tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
'''
#7.2
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter ' quit ' to end the program. "
active = True
while active:
    message = input(prompt)
    
    if message != 'quit':
        print(message)
    else:
        active = False
'''
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter ' quit ' to end the program. "
while True:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        break
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
#7.3
'''
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("\nPlease enter your name: ")
    response = input("\nWhich mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person response?(yes/no) ")
    if repeat == "no":
        polling_active = False
print("\n-- Poll Results --")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
'''
#No.8
#8.1
def greet_user():
    print("Bonjour!")
greet_user()
def greet_user_1(username):
    print("\nBonjour! " + username.title() + ".")
greet_user_1("marvin")
#8.2
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
describe_pet("dog", "dortmund")
describe_pet("cat", "bayern")
def describe_pet_1(animal_type, pet_name):
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
describe_pet_1(animal_type='hamster', pet_name='paris')
describe_pet_1(pet_name='Madrid', animal_type='sheep')
def describe_pet_2(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
describe_pet_2(pet_name='Man')
describe_pet_2('Che')
describe_pet_2('Liv', 'tiger')
describe_pet_2(animal_type='tiger', pet_name='Liv')
#8.3
def get_formatted_name(first_name, last_name):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
def get_formatted_name_1(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name.title() + ' ' + middle_name.title() + ' ' + last_name.title()
    else:
        full_name = first_name.title() + ' ' + last_name.title()
    return full_name
musician = get_formatted_name_1('jimi', 'hendrix')
print(musician)
musician = get_formatted_name_1('john', 'hooker', 'lee')
print(musician)
def build_person(first_name, last_name):
    person = {'first':first_name.title(), 'last':last_name.title()}
    return person
musician = build_person('jimi', 'hendrix')
print("\nMy favorite musician is " + musician['first'] + " " + musician['last'])
def build_person_1(first_name, last_name, age=''):
    person = {'first':first_name.title(), 'last':last_name.title()}
    if age:
        person['age'] = age
    return person
musician = build_person_1('jimi', 'hendrix', 27)
print("\nMy favorite musician is " + musician['first'] + " " + musician['last'])
print("He is " + str(musician['age']) + " year's old")