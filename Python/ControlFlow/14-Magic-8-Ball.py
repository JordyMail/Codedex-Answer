import random

1 == "Yes - definitely."
2 == "It is decidedly so."
3 == "Without a doubt."
4 == "Reply hazy, try again."
5 == "Ask again later."
6 == "Better not tell you now."
7 == "My sources say no."
8 == "Outlook not so good."
9 == "Very doubtful."

question = input("Enter your Question: ")

num = random.randint(1,9)
print("Magic Ball: " + num)
