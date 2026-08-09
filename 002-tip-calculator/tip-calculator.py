print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = float(input("How much would you like to tip? 10, 12 or 15?\n"))
people = float(input("How many people to split the bill?\n"))
tips_as_percent = tip / 100
total_tip_amount = bill * tips_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")
