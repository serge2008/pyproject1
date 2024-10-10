numBottles = int(input("Enter the number of bottles you deposit: "))
deposit = 0

for i in range(numBottles):
    VolumeL = float(input("Enter the volume of the bottle in liters: "))
    if VolumeL <= 1:
        deposit += 0.10
    else:
        deposit += 0.25

# Format the deposit value with two decimal places
formatted_deposit = "{:.2f}".format(deposit)
print("Total deposit amount: $" + formatted_deposit)