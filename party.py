userinput = input("How long to the party ?")
usernum = int(userinput)

if usernum < 1:
    print("Party Now")
else:
    for i in range(usernum, 0, -1):
        print(i)
    if i == 1:
        print("PARTY TIME!!!")
