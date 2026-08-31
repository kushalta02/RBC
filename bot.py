import re


# ============================================================
# 1. CHATBOT STATE
# ============================================================

state = {
    "intent": None,
    "items": [],
    "quantity": None,
    "sugar": None,
    "name": None
}


# ============================================================
# 2. INTENT DETECTION
# ============================================================

def detect_intent(text):

    text = text.lower()

    # Greeting
    if any(word in text for word in [
        "hi", "hello", "hey", "hii", "helo"
    ]):
        return "greeting"

    # Goodbye
    if any(word in text for word in [
        "bye", "goodbye", "see you", "exit", "quit"
    ]):
        return "goodbye"

    # Thanks
    if any(word in text for word in [
        "thanks", "thank you", "thx"
    ]):
        return "thanks"

    # Order
    if any(word in text for word in [
        "want", "order", "give me", "i need",
        "buy", "get me"
    ]):
        return "order"

    # Coffee
    if "coffee" in text:
        return "order"

    # Pizza
    if "pizza" in text:
        return "order"

    # Name
    if "my name is" in text or "i am" in text:
        return "name"

    return "unknown"


# ============================================================
# 3. ENTITY EXTRACTION
# ============================================================

def extract_entities(text):

    text = text.lower()

    entities = {}

    # -------------------------
    # Quantity
    # -------------------------

    number_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    quantity = None

    # Check digits
    match = re.search(r"\b(\d+)\b", text)

    if match:
        quantity = int(match.group(1))

    # Check number words
    if quantity is None:
        for word, number in number_words.items():
            if word in text:
                quantity = number
                break

    if quantity:
        entities["quantity"] = quantity


    # -------------------------
    # Item
    # -------------------------

    if "coffee" in text:
        entities["item"] = "coffee"

    elif "pizza" in text:
        entities["item"] = "pizza"


    # -------------------------
    # Sugar
    # -------------------------

    if "without sugar" in text or "no sugar" in text:
        entities["sugar"] = "without sugar"

    elif "with sugar" in text:
        entities["sugar"] = "with sugar"


    # -------------------------
    # Name
    # -------------------------

    match = re.search(
        r"(?:my name is|i am|i'm)\s+([a-zA-Z]+)",
        text
    )

    if match:
        entities["name"] = match.group(1).capitalize()


    return entities


# ============================================================
# 4. UPDATE STATE
# ============================================================

def update_state(intent, entities):

    state["intent"] = intent

    if "quantity" in entities:
        state["quantity"] = entities["quantity"]

    if "name" in entities:
        state["name"] = entities["name"]

    if "item" in entities:

        item = {
            "name": entities["item"],
            "sugar": entities.get("sugar")
        }

        state["items"].append(item)

    elif "sugar" in entities:

        # User is continuing previous order
        if state["items"]:

            state["items"][-1]["sugar"] = entities["sugar"]


# ============================================================
# 5. RESPONSE GENERATION
# ============================================================

def generate_response(intent, entities):

    # -------------------------
    # Greeting
    # -------------------------

    if intent == "greeting":

        if state["name"]:
            return f"Hello {state['name']}! How can I help you?"

        return "Hello! How can I help you?"


    # -------------------------
    # Name
    # -------------------------

    if intent == "name":

        if state["name"]:
            return f"Nice to meet you, {state['name']}!"

        return "Nice to meet you!"


    # -------------------------
    # Order
    # -------------------------

    if intent == "order":

        item = entities.get("item")
        quantity = entities.get("quantity")

        # New order
        if item:

            if quantity:
                return f"Sure! You want {quantity} {item}(s). Anything else?"

            return f"Sure! You want {item}. How many would you like?"


        # User only gave quantity
        if quantity and state["items"]:

            return (
                f"Got it. I'll add {quantity} "
                f"{state['items'][-1]['name']}(s)."
            )

        # User only gave sugar preference
        if "sugar" in entities:

            return (
                f"Got it — {entities['sugar']}."
            )

        return "Sure! What would you like to order?"


    # -------------------------
    # Thanks
    # -------------------------

    if intent == "thanks":

        return "You're welcome!"


    # -------------------------
    # Goodbye
    # -------------------------

    if intent == "goodbye":

        return "Goodbye! Have a great day!"


    # -------------------------
    # Unknown
    # -------------------------

    return (
        "Sorry, I didn't understand that. "
        "You can ask me to order coffee or pizza."
    )


# ============================================================
# 6. DISPLAY STATE
# ============================================================

def show_state():

    print("\n----- CURRENT STATE -----")
    print("Intent :", state["intent"])
    print("Name   :", state["name"])
    print("Items  :", state["items"])
    print("-------------------------\n")


# ============================================================
# 7. MAIN CHAT LOOP
# ============================================================

print("🤖 Bot: Hello! I'm your chatbot. Type 'bye' to exit.")

while True:

    user_input = input("You: ")

    # -------------------------
    # Intent
    # -------------------------

    intent = detect_intent(user_input)

    # -------------------------
    # Entities
    # -------------------------

    entities = extract_entities(user_input)

    # -------------------------
    # State
    # -------------------------

    update_state(intent, entities)

    # -------------------------
    # Response
    # -------------------------

    response = generate_response(intent, entities)

    print("🤖 Bot:", response)

    # Uncomment this if you want
    # to see what chatbot understood

    # print("Intent:", intent)
    # print("Entities:", entities)
    # show_state()

    # -------------------------
    # Exit
    # -------------------------

    if intent == "goodbye":
        break