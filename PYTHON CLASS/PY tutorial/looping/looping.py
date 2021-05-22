for i in range(1,100):
    if i % 2 ==0:
        print(i)

for i in range(3,99):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        print(i)


        
z = int(input("To what range: "))
for i in range(1,z):
    for a in range(1,z):
        b = i * a
        print(i,"x",a,"=",b)
        
