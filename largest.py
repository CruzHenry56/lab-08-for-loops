a= []
num = int(input("Enter the range of numbers: "))
for i in range (1,num+1):
    b=int(input("Enter a number: "))
    a.append(b)
a.sort()
print("The Largest number is:",a[num-1])
