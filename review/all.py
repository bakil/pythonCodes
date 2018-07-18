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


# thistuple = ("apple", "banana", "cherry") ## Tuple is ordered but unchangeable
# #thistuple[1] = "blackcurrant" # test changeability ==> will not change
# thisset= { "apple", "banana", "cherry"} # Unordered and unindexed
# thisdict = {"apple": "green","banana": "yellow", "cherry": "red"} # keys and values
# thislist = ["apple", "banana", "cherry"]
# list2 = thislist.insert(1,"new") ## ['apple', 'new', 'banana', 'cherry'] , 
# #note how inser new value and shift list
# #print thislist
# #print list2 ## None  , note dont use assienment = at the same time with list method
# mylist1= [1,"bakil", 35, ["sima","shadeen","kanan"]] ## [1, 'bakil', 35]
# #print mylist1[:3] ## [1, 'bakil', 35]
# #print mylist1.index(35) ## 2
# #print range(1,100,10) ## [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
# mylist1.remove("bakil") ## [1, 35, ['sima', 'shadeen', 'kanan']]  
# """ we use remove when we know the item which we want to delete, or use del() if we know index """
# ## if item not in the list, there will be an error
# mylist2 = [3,5,7,9,2]
# del(mylist2[1])
# #print mylist2  ## [3, 7, 9, 2]
# mytext1 = "hi dad"
# del(mytext1[1]) ## TypeError: 'str' object doesn't support item deletion
# #print mytext1
# #print mylist1
# nolist =list("123456789") ## note how to convert str to list
# #print nolist ## ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# mylist3 = [4,2,8,9,5,7]
# print len(mylist3) ## 6
# print max(mylist3) ## 9
# print min(mylist3) ## 2
# print sum(mylist3) ## 35
animal=['cat', 'dog', 'rabbit']
# animal.append("tiger") ## ['cat', 'dog', 'rabbit', 'tiger'] , Add Single Element to The List
# #print animal
# print animal.count("cat") ## 1 ,  count of how many times obj occurs in list
# print animal.index("cat") # 0
bird=["dee","bee"]
animal.extend(bird) ## Add listElements to The List
print animal
# animal.insert(0,"first") ## ['first', 'cat', 'dog', 'rabbit', 'tiger'] , insert to position with shifting
# #print animal
# print animal.pop() ## tiger , normally pop(-1) will remove the last item and return it
# #print animal ## ['first', 'cat', 'dog', 'rabbit'] , without tigger
# print animal.pop(2) ## dog pop intem in index2 2
# #print animal ## ['first', 'cat', 'rabbit'] without dog
# animal.remove( "cat") ## just remove withourreturn any thing
# #print animal ## ['first', 'rabbit'] without cat
# animal.reverse() ## reverse the list
# #print animal ## ['rabbit', 'first']
# animal.sort() ## sort item A-Z
# #print animal ## ['first', 'rabbit']
# animal.sort(reverse = True)# just like sort()+reverse()
# print animal
