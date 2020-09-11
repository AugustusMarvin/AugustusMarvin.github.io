#10.1
with open('E:\python_wenjian\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
file_name = 'E:\python_wenjian\pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip() + "\n")
print(lines[1].rstrip())
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string) 
print(len(pi_string))
print(pi_string[:22] + "...\n")
print(len(pi_string))

file_name = 'E:\python_wenjian\programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I don't love programming.\n")
    file_object.write("I love creating new games!")
with open(file_name, "a") as file_object:
    file_object.write("\nI also find love finding meaning in large daratasets.\n")

file_name = 'E:\python_wenjian\programming_1.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I don't love programming.\n")
    file_object.write("I love creating new games!")
with open(file_name, "a") as file_object:
    file_object.write("\nI also find love finding meaning in large daratasets.\n")

#10.2程序崩溃时处理
'''
print("Give two numbers, and I'll divide them.")
print("Enter 'q' to quit!!")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You just can't divide by 0!! ")
    else:
        print(answer)
    '''
file_name_1 = 'alice.txt'
try:
    with open(file_name_1) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name_1 + "dose not exist!"
    print(msg)
else:
    print(contents)
file_name_1 = 'alice.txt'
try:
    with open(file_name_1) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    print(contents)
#10.3存储数据
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'E:/python_wenjian/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)