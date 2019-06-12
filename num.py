m=['a','e','i','o','u']
a=input()
if(m.count(a)!=0):
    print("Vowel")
elif(a.isalpha()):
    print("Consonant")
else:
    print("invalid")
