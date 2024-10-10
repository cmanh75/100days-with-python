import random

word_list = ["camel", "sugar", "orange", "eagle", "panther", "green", "tiger"]

chosen_word = random.choice(word_list)

place_holder = ""
game_over = False
lives = 6

for i in range(0, len(chosen_word)):
    place_holder += "_"

correct_letter = []

print("Word to guess: " + place_holder)

while not game_over:
    guess = input("Guess a letter: ").lower()
    exist = False
    display = ""
    if guess in correct_letter:
        print("The letter has been existed. Guess Again!")
        continue
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess or chosen_word[i] in correct_letter:
            display += chosen_word[i]
        else:
            display += '_'
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives > 0:
            print(f"You have only {lives} lives left")
    else:
        correct_letter.append(guess)
    if lives < 0:
        print("You lose")
        game_over = True
    if '_' not in display:
        print("You Win")
        game_over = True
    



