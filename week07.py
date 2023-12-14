largest = None
smallest = None

while True:
    snum = input('Enter integer number: ')
    if snum == 'done':
        break

    try:
        inum = int(snum)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = inum
    if smallest is None:
        smallest = inum

    if inum>largest:
        largest = inum
    if inum<smallest:
         smallest = inum
    
print('Maximum is', largest)
print('Minimum is', smallest)
