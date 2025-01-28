print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = bill * (tip/100)
cost_tax_each = round((total / people), 3)
cost_main_each = bill / people
cost_each = cost_main_each + cost_tax_each
print(f"You will pay {cost_each} each")
