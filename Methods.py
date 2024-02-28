#String Methods
S="ankit kumar"
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
