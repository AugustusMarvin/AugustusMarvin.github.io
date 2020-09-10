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
    file_object.write("I love programming.")

