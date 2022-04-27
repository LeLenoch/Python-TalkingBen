import random
print('Ben: Ben?')
while True:
    question = input("You: ")
    j = ["Yes.", "No.", "Hohoho!", "Ugh.."]
    print(f'Ben: {random.choice(j)}')
