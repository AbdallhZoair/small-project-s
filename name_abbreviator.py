# i know this code not clean ... but i happy about it
name_f = input("Enter The first and last name of  your  sepatated by a comma : ").split(", ")
name=[]
first_name = []
first_l = []

second_name = [] # i don't use it put i let him if i need it
second_l = []    # i don't use it put i let him if i need it

for x in range(len(name_f)):
 A = name_f[x]
 A=A.split(" ")
 name.append(A)

 first_name.append(name[x][0])
 first_l.append(first_name[x][0])

 second_name.append(name[x][1])
 second_l.append(second_name[x][0])

print(name)


print("\nAbbreviated name : ")
for x in range(len(name)):
    print(f"{first_l[x]}.{second_l[x]}")


