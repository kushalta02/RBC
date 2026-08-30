#logic to reply until user says bye
while True:
    user_message=input("You: ")
    if user_message=="bye":
        print("Bot: Goodbye!")
        break
    print(f"Bot : What can i do for you?")