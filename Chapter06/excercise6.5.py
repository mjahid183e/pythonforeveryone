print('Exercise 6.5')

str = 'M Jahidul:4545 Islam'

print(str)
colonfound = str.find(':')
print(colonfound)

newstr = str[colonfound+1:14]
print(newstr)

fltnbr = float(newstr)
print(fltnbr)

print('file problem:')
stuff = 'Amar sunar bangla\nami tumay valobashi'
print(stuff)