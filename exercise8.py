meal_cost = float(input("Enter the cost of the meal: $"))
tax_rate = 0.13
tax_amount = meal_cost * tax_rate
tip_rate = 0.18
tip_amount = meal_cost * tip_rate
grand_total = meal_cost + tax_amount + tip_amount
formatted_tax = "{:.2f}".format(tax_amount)
formatted_tip = "{:.2f}".format(tip_amount)
formatted_total = "{:.2f}".format(grand_total)
print("Tax amount: ",formatted_tax)
print("Tip amount: ",formatted_tip)
print("Grand total: ",formatted_total)