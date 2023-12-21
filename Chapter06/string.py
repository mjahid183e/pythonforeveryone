fruit = "banana"
index =0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

print("Using for loop")
for i in fruit:
    print(i)

# python has lots of string functions
name = "Hello Jahid sdfdkjf2df df@df df"
uname = name.upper()
print(uname)
print(name)
print(type(name))
print(dir(uname))

nname = name.replace('o', 'w')
print(nname)
found_index = name.find('@')
print(found_index)

found_index1 = name.find(' ', found_index)
print(found_index1)