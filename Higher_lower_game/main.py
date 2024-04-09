#import statements
from art import logo
import random
from art import vs
from game_data import data
from clear import clear

#scoretracker
score = 0

#list for number already generated
past_num = []

game_playing = True

#for tracking index
index = 0


# Since we have no inbuilt function to generate random number within given range except some number in that range, we have to create it
def index_gen():
    global index
    while index in past_num:
        index = random.randint(0, len(data) - 2)
    past_num.append(index)
    return index


# We could have choosen a random.shuffle(data) to shuffle data list in random order rather than calling the above function again and again

for _ in range(len(data) - 1):
    print(logo)
    # for option A
    numA = index_gen()
    print(
        f"Compare A:{data[numA]['name']}, a {data[numA]['description']}, from {data[numA]['country']}."
    )
    print(vs)
    #for option B
    numB = index_gen()
    print(
        f"Against B:{data[numB]['name']}, a {data[numB]['description']}, from {data[numB]['country']}."
    )
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a" and data[numA]['follower_count'] > data[numB][
            'follower_count']:
        score += 1
        clear()
        print(f"You're right! Current score: {score}")
    elif answer == "b" and data[numA]['follower_count'] < data[numB][
            'follower_count']:
        score += 1
        clear()
        print(f"You're right! Current score: {score}")
    else:
        print("You made a wrong choice.")
        quit()

print(f"Woo... you won! You scored {score}")
