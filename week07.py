largest = None
smallest = None

while True:
    snum = input('Enter integer number: ')
    if snum == 'done':
        break

    try:
        fnum = float(snum)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = fnum
    if smallest is None:
        smallest = fnum

    if fnum>largest:
        largest = fnum

    if fnum<smallest:
         smallest = fnum
    
print('Maximum', largest)
print('Minimum', smallest)
