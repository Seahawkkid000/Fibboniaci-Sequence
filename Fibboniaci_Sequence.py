number=int(input("Enter a number"))
i=0
j=1
print(i,",",j, end=", ")
for a in range(2,number):
    h=i+j
    print(j, end=", ")
    i=j
    j=h

