PLACE_HOLDER = "[name]"

with open("./day24/Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()
with open("./day24/Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    form = starting_letter.read()

for name in names:
    letter_for_name = form
    name = name.strip()
    letter_for_name = letter_for_name.replace(PLACE_HOLDER, name)
    with open(f"./day24/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        letter.write(letter_for_name)
