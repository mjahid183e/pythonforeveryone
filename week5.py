hrs = input("Enter Hours:")
rph = input("Enter rate_per_hour:")
pay = float(hrs)* float(rph)
print('Pay:', pay)

astr = "Hi there!"
try:
    istr = int(astr)
except:
    istr = -1

print("First ", istr)

bstr = "123"
try:
    estr = int(bstr)
except:
    estr = -1

print("Second", estr)
