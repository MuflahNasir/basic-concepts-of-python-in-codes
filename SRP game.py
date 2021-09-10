import random

number = random.randint(0,2)

if number == 0:
    tool = "scissor"
elif number == 1:
    tool = "rock"
else:
    tool = "paper"

guess = eval(input("Choose scissor (0), rock (1) and paper (2): "))

if guess == 0 and number == 0:
    print("Computer is ",tool,". You are scissor too. Game is draw!!!!")
elif guess == 0 and number == 1:
    print("Computer is ",tool,". You are scissor. You lose!!!!")
elif guess == 0 and number == 2:
    print("Computer is ",tool,". You are scissor. You won!!!!")
elif guess == 1 and number == 0:
    print("Computer is ",tool,". You are rock. You won!!!!")
elif guess == 1 and number == 1:
    print("Computer is ",tool,". You are rock too. Game is draw!!!!")
elif guess == 1 and number == 2:
    print("Computer is ",tool,". You are rock. You lose!!!!")
elif guess == 2 and number == 0:
    print("Computer is ",tool,". You are paper. You lose!!!!")
elif guess == 2 and number == 1:
    print("Computer is ",tool,". You are paper. You won!!!!")
elif guess == 2 and number == 2 :
    print("Computer is ",tool,". You are paper too. Game is draw!!!!")
else:
    print("Invalid guess")
