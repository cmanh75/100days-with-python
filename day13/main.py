import art
import gamedata
import random

objects = gamedata.data

print(art.logo)
object_A = random.choice(objects)
scores = 0

while True:
    object_B = random.choice(objects)
    while object_A == object_B:
        object_B = random.choice(objects)
    print(f"Compare A: {object_A['name']}, {object_A['description']}, from {object_A['country']}")
    print(art.vs)
    print(f"Against: {object_B['name']}, {object_B['description']}, from {object_B['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    print("\n" * 20)   
    print(art.logo) 
    right_choice = object_A
    if right_choice['follower_count'] < object_B['follower_count']:
        right_choice = object_B
    if answer == "A":
        if object_A['follower_count'] < right_choice['follower_count']:
            print(f"Sorry, that's wrong. Final score: {scores}")
            break
    else:
        if object_B['follower_count'] < right_choice['follower_count']:
            print(f"Sorry, that's wrong. Final score: {scores}")
            break
    scores += 1
    print(f"You're right! Current score: {scores}")
