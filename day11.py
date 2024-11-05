import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
human_deck = []
dealer_deck = []

def scores_of_deck(deck):
    scores = 0
    for card in deck:
        scores += card
    return scores

def gen_card(deck):
    card = random.choice(cards)
    deck.append(card)
    scores = scores_of_deck(deck)
    while scores > 21:
        ok = True
        for ind in range(0, len(deck)):
            if deck[ind] == 11:
                deck[ind] = 1
                ok = False
        if ok == True:
            break

gen_card(human_deck)
gen_card(human_deck)

gen_card(dealer_deck)
gen_card(dealer_deck)
while (scores_of_deck(dealer_deck) < 17):
    gen_card(dealer_deck)

def output_human():
    print(f"Your deck is {human_deck} and your scores are {scores_of_deck(human_deck)}")

output_human()
print(f"The first card of dealer deck is {dealer_deck[0]}")

while True == True:
    choice = input("Do you want draw a card? type 'yes' or 'no': ")
    if choice == "no":
        break
    else:
        gen_card(human_deck)
        output_human()
        if (scores_of_deck(human_deck) > 21):
            break

if scores_of_deck(human_deck) > 21:
    print("You lose! Because your scores over 21")
else:
    output_human()
    print(f"Dealer's deck is {dealer_deck} ans dealer's scores are {scores_of_deck(dealer_deck)} ")
    if scores_of_deck(dealer_deck) > 21:
        print("You win! Because dealer's scores over 21!")
    else:
        if scores_of_deck(dealer_deck) > scores_of_deck(human_deck):
            print("You lose! Because your scores are less than dealer's scores")
        elif scores_of_deck(dealer_deck) < scores_of_deck(human_deck):
            print("You lose! Because your scores are more than dealer's scores")
        else:
            print("Draw")
    
