# find("str", startIndex, stopIndex), count("str"), len(str)
# 
a= "hi"
b= "nonnnnnnono"
print b.find("o",2,9) ## 8
print b.index("o") ## 1   just as find
print b.count("o") ## 3
print len(a) ## 2
print "hi mam".isalnum() ## False  because of space
print "hi mam".rjust(10) ## right justifcation
print "hi mam".ljust(10)+"x" ## left justifcation
print "".join(["a", "b"]) ## ab  use join to convert list to string
print "--".join(["a", "b", "c"]) ## a--b--c
print " ".join(["I", "love", "you"]) ## I love you
print "I love you".split(" ") ## ['I', 'love', 'you']
#splitlines()
if "hi" in "hi wourld":
    print "yes" 
print "hi mam".capitalize() ## Hi mam  , It will capitalize the first letter inside a string
print "hi mam".upper() ## HI MAM   , converts all of the characters to uppercase
print "HELLO WORLD".lower() ## hello world  , converts all of the characters to lowercase
print "hello world".replace("l","X") ## heXXo worXd  replace all Ocurance
print "hello world".replace("l","") ## heo word
print "hello world".replace("l","",2) ## heo world  , only the first two occurance
a="ali"
b=a.replace("a","w") # only returned value will change
print a , b # ali wli note that value of a was not affected by method replace.
print "hello world".center(20,"=") ## ====hello world=====
print "".center(20,"=") ##            ====================
print "hello world".endswith("ld") ## True
## role for string the none character "" is avalible before andafter any character
print a.find("",1) ## 1
print a.find("") ## 0
print a.find("",2) ## 2
print a.find("",3) ## -1
print a[-1:]## i
print a[:6] ## hi
print a[6:] ## None but not error
print a[6:9] ## IndexError: string index out of range
print a.find("H") ## -1 Python is case sensitive that means there is a diffrence between uppercase and lowercase letters 
a=""
#print a[0] ## IndexError: string index out of range
print a[0:] ## None but not error
#print a[0] ## return error
a = "hello"
b = "world"
c = 5
print a + " "+ b ## hello world
print a,b ## hello world , will be separated by space
print a,c ## hello 5 , it ok to print string and int in this way
#print a + c ## TypeError: cannot concatenate 'str' and 'int' objects
# Be careful: In python you cannot concatenate a string with an integer (number) 
print a * c ## hellohellohellohellohello   multiply string and int will repeat it
#print a / c ## TypeError: unsupported operand type(s) for /: 'str' and 'int'