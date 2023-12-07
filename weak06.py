def computepay(h, r):
    if h <= 40:
        gross_pay = h*r

    else:
        regular_hours = 40
        over_time = h - regular_hours
        gross_pay = (regular_hours*r) + (over_time*r*1.5)
        
        return gross_pay

hrs = input("Enter hours: ")
fhrs = float(hrs)
rate = input("Enter rate per hour: ")
frate = float(rate)

print("Pay", computepay(fhrs, frate))
