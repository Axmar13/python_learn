import random
num = random.randint(1, 9)

question = input("Question: ")

if num == 1:
    print("Magic 8 ball: Yes - definitely.")
elif num == 2:
    print("Magic 8 ball: It is decidedly so.")
elif num == 3:
    print("Magic 8 ball: Without a doubt.")
elif num == 4:
    print("Magic 8 ball: Reply hazy, try again.")
elif num == 5:
    print("Magic 8 ball: Ask again later.")
elif num == 6:
    print("Magic 8 ball: Better not tell you now.")
elif num == 7:
    print("Magic 8 ball: My sources say no.")
elif num == 8:
    print("Magic 8 ball: Outlook not so good.")
else:
    print("Magic 8 ball: Very doubtful.")