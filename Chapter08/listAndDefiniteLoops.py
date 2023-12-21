# Use of range function
print(range(5))
friends = ['Jahid', 'Rafat', 'Al Amin']
print(len(friends))
print(range(len(friends)))

for friend in friends:
    print('Happy new year:', friend)

# Again similar things can be done using range function, but I'll be uisng first one
for i in range(len(friends)):
    friend = friends[i]
    print('Hay, happy new year:', friend)

# Lists can be sliced using : :
print(friends[0:2])

print('Print the whole list: ', friends[:])
print('Type of the class: ',type(friends))
print('Operations can be done with Lists: ',dir(friends))

# We can create an empty list and then add elements using the apppend method:

institutes = list()
institutes.append('NSU' )
institutes.append('DU')
institutes.append('BUET')
print(institutes[:])

# Python provides two operators that let you check if an item is in a list, "in and not in", these are logical operators that return True or False, but they do not modity the list
print("Checking, NSU in the list?",'NSU' in institutes)
print("MIST in the list?", 'MIST' not in institutes)

# Sorting a list
institutes.sort()
print('The sorted list is:',institutes)
print('But the number one uni in Bangladesh is:', institutes[2])

# Some other built in functions are len, max, min, sum etc.
# Practice of Creating a list form user inputs and calculating its avg with try and except
numlist = list()
while True:
    num=input('Enter a number: ')
    if num == 'done':
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input, please enter a number')
        continue
    numlist.append(fnum)
print('The list is: ', numlist)

avg = sum(numlist) / len(numlist)
print('The average of the list is: ', avg)