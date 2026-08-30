# Rule-Based Restaurant Chatbot

def menu():
    return "1. Pizza\n2. Burger\n3. Pasta\n4. Salad"


def take_order():

    # Ask for order item
    user_order = input("Bot: What would you like to order? ").lower().strip()

    # Check if item is available
    if user_order in ["pizza", "burger", "salad", "pasta"]:

        # Ask quantity
        quantity = input(
            "Bot: How much quantity do you want to have? "
        ).strip()

        # Ask for customization
        customize = input(
            "Bot: Would you like to customize your order? (yes/no) "
        ).lower().strip()

        # If user wants customization
        if customize in ["yes", "yeah", "yup", "sure"]:

            customization = input(
                "Bot: Please let me know your customizations: "
            ).strip()

            print(
                f"Bot: Your order of {user_order} "
                f"with quantity {quantity} "
                f"and customization '{customization}' "
                f"has been placed successfully!"
            )

        # If user doesn't want customization
        elif customize in ["no", "nope", "nah"]:

            print(
                f"Bot: Your order of {user_order} "
                f"with quantity {quantity} "
                f"has been placed successfully!"
            )

        # Invalid customization response
        else:
            print(
                "Bot: Please answer with yes or no."
            )

    else:
        print(
            "Bot: Sorry, that item is not available. "
            "Please choose from pizza, burger, pasta, or salad."
        )


# Main chatbot loop
while True:

    user_message = input("You: ").lower().strip()

    # Greeting
    if user_message in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        intent = "greeting"
        print("Bot: Hello! How can I assist you today?")

    # How are you
    elif user_message in [
        "how are you",
        "how are you doing",
        "how's it going"
    ]:
        intent = "how_are_you"
        print("Bot: I'm doing well, thank you for asking!")

    # Menu
    elif user_message in [
        "menu",
        "show menu",
        "what do you have",
        "what can i order",
        "i want to see the menu",
        "i want food"
    ]:
        intent = "menu"
        print("Bot: Here is our menu:")
        print(menu())

    # Order
    elif user_message in [
        "order",
        "i want to order",
        "i would like to order"
    ]:
        intent = "order"
        take_order()

    # Exit
    elif user_message == "bye":
        intent = "exit"
        print("Bot: Goodbye!")
        break

    # Unknown input
    else:
        intent = "unknown"
        print("Bot: Sorry, I don't understand that.")