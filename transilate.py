
from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab) # use it to create transilation
str = "this is string example....wow!!!";
print str.translate(trantab) ##  th3s 3s str3ng 2x1mpl2....w4w!!!

a = "How are you"
b=a.translate(None,"o") ## here we don't use table transilate but we delete char o
print b ## Hw are yu