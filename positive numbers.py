
NumList = []
Positive = []

Number = int(input("Please enter the Total Number of List Elements : "))
for n in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %n))
    NumList.append(value)

for m in range(Number):
    if(NumList[m] >= 0):
        Positive.append(NumList[m])

print("Element in Positive List is : ", Positive)
