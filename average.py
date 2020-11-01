num = int(input("How many number?: "))
total_sum = 0

for n in range(num):
    numbers=float(input("Please enter a number "))
    total_sum += numbers

avg = total_sum / num
print("Average is ", avg)
