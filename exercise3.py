numNumbers=int(input("enter # of marks: "))
total=0
for i in range(numNumbers):
    total=total+int(input("enter %: "))
average=total/numNumbers
print ("your average is: ",average,"%")