#String Methods
S="ankit kumar {Age}"
P=" mihir dutta"
print(S.capitalize())#Capitalize first Letter
print(S.count("a"))#Count nubmer of occurence
print(S.endswith("r"))#Check the value ends with the particular character or not.
print(P.isupper())#Check the particular String is capital or not.
print(P.islower())#Check the particular String is small or not.
print(P.find("u"))#Finds the character in the given String
print(P.lower())#Lower the case of whole String
print(S.upper())#Capitalize whole String
print(P.strip())#remove extra unusual things
print(P.startswith("k"))#Check The Stsrting of string with particular character or not
print(S.replace("a","A"))#Replace the character from new Character
print(P.title())#Capitalize first letter of each word in string
print(S.split())#Make the list of the String
print(S.center(20))#Align the return String in center
print(S.format(Age=19))#Add the value in the string

#List Methods
li=["a","b","c"]
li1=["e","f","g"]
li.append("d")#adds the value from last index
print(li)
li.remove("a")#Remove the value from list
print(li)
li.extend(li1)#Extends li1 in li
print(li)
li.insert(1,"z")#Insert the value in between
print(li)
li.pop()#Removes Last Element
print(li)
print(len(li))#Checks the length of the function

#set methods
A={"a","b","c"}
B={"c","e","f"}
A.add("d")#add the value in the set
print(A)
A.remove("b") #remove the element from the set
print(A)
print(A.union(B)) #Union two set
print(A.intersection(B)) #Find common value from two sets

#Dictionary Methods
C={1:"Ankit",2:"Mine"}
print(C.keys()) #print all the keys
print(C.values()) #print all the values
print(C.items()) #items shows in the form of list
print(C.get(2)) #Get the value of any key
C.update({3:"Anyone"})#Add new element in a dictionary
print(C)
