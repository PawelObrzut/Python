def computepay(h,r):
    if h <= 40:
        pay = r*h
        return pay
    else:
        pay = r*40 + (r*1.5* (h-40))
        return pay


hrs = raw_input("Enter Hours:")
h = float(hrs)
rt = raw_input ("Enter Rate: ")
r = float(rt)

print computepay(h,r)