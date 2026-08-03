import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = int(input("Enter Your Number : "))

        if user_num == lucky_num:
            print("You Win")
            break
        elif user_num < lucky_num:
            print("Your Number is Low")
        elif user_num > lucky_num:
            print("Your Number is High")


play_game()
print("Game Over , Thanks For Playing")

