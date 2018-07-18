# print 5%2                ## 1
# print 5**2               ## 25
# print 5/2                ## 2
# print -5/2               ## -3
# print 5//2
# print -5//2
# a=2
# a**=3  ## a=a**3
# print a
# print 5^2 ## 7,  101 xor 010 = 111 == 7

a = [30,4]
b = [5,7]
a=b
a.append(6)
print a,b

if ( a is b ):
   print "Line 1 - a and b have same identity"
else:
   print "Line 1 - a and b do not have same identity"
