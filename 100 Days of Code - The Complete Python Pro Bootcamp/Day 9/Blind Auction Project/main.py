# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
bid_price = {}
yes_or_no = True
highest = 0
# TODO-3: Whether if new bids need to be added
while yes_or_no == True:
    name = input("what is your name for bidding :")
    price = int(input("How much you going to bid :"))
    bid_price[name] = price
    more_bid = input("Have another bid? yes or no :")
    if more_bid == "no":
        yes_or_no = False
    elif more_bid == "yes":
        print("\n"*20)

# TODO-4: Compare bids in dictionary
for key in bid_price:
    bid_amount = bid_price[key]
    if bid_amount > highest:
        highest = bid_amount
        winner = key

print(f"winner is {winner} by {highest}$")
