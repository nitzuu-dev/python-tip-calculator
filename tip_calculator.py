# Tip Calculator

# Get user input for bill and tip percentage
user_bill = input("Enter the total bill: ")
user_tip = input("Enter tip percentage: ")

# Convert inputs to float
bill = float(user_bill)
tip_percent = float(user_tip)

# Calculate tip and total
tip_amount = bill * (tip_percent / 100)
total_pay = bill + tip_amount

# Print results
print("You should tip: " + str(round(tip_amount, 2)))
print("Total amount to pay: " + str(round(total_pay, 2)))
