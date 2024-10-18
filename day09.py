bids = {}
continue_bidding = True
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while (continue_bidding):
    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        find_highest_bidder(bids)
        continue_bidding = False
    else:
        print("\n" * 20)
