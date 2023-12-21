fhand = open('Jahid.txt', 'r')
count = 0
for line in fhand:
    count = count + 1
    line = line.rstrip()
    if line.startswith('Weekend'):
        print(line)
print('Total line: ', count)

print('Print length of the file:')
slength = fhand.read()
print(len(slength))
print(slength[:4])

print('Solving the problem in a different way:')
fname = input('Enter the file name: ')
try:
    fobject = open(fname)
except:
    print('File can not be open', fname)
    quit()

count01 = 0
for line in fname:
    if line.startswith('Pawruti'):
        count = count+1
print('There were', count, 'subject line in', fname)