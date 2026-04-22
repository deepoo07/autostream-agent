import json

# Load knowledge base
with open("local_knowledge_base(RAG).json") as f:
    data = json.load(f)

# Mock tool
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")

# Validation
def is_valid_email(email):
    return "@" in email and "." in email

# Intent detection
def detect_intent(text):
    text = text.lower()

    if "hi" in text or "hello" in text:
        return "greeting"
    elif "buy" in text or "subscribe" in text or "want" in text or "try" in text:
        return "high_intent"
    else:
        return "pricing"

# RAG
def rag_response(query):
    query = query.lower()

    if "basic" in query:
        return f"""
Basic Plan:
Price: {data['basic_plan']['price']}
Features: {", ".join(data['basic_plan']['features'])}
"""
    elif "pro" in query:
        return f"""
Pro Plan:
Price: {data['pro_plan']['price']}
Features: {", ".join(data['pro_plan']['features'])}
"""
    elif "price" in query or "pricing" in query or "plan" in query:
        return f"""
Basic: {data['basic_plan']['price']}
Pro: {data['pro_plan']['price']}
"""
    elif "feature" in query:
        return f"""
Basic Features: {", ".join(data['basic_plan']['features'])}
Pro Features: {", ".join(data['pro_plan']['features'])}
"""
    elif "polic" in query or "refund" in query:
        return "\n".join(data["policies"])
    else:
        return "Please ask about pricing, features, or policies."

# State
conversation_state = {"stage": "start"}
lead_data = {"name": None, "email": None, "platform": None}

# Agent
def agent(user_input):
    text = user_input.lower()

    if conversation_state["stage"] == "ask_name":
        lead_data["name"] = user_input
        conversation_state["stage"] = "ask_email"
        return "Enter your email"

    elif conversation_state["stage"] == "ask_email":
        if not is_valid_email(user_input):
            return "Please enter a valid email (example: name@gmail.com)"

        lead_data["email"] = user_input
        conversation_state["stage"] = "ask_platform"
        return "Which platform do you use? (YouTube, Instagram, TikTok, Facebook, LinkedIn)"

    elif conversation_state["stage"] == "ask_platform":
        allowed_platforms = ["youtube", "instagram", "tiktok", "facebook", "linkedin"]

        if text not in allowed_platforms:
            return "Please choose from: YouTube, Instagram, TikTok, Facebook, LinkedIn"

        lead_data["platform"] = user_input

        mock_lead_capture(
            lead_data["name"],
            lead_data["email"],
            lead_data["platform"]
        )

        conversation_state["stage"] = "post_lead"
        return "Thanks! We will contact you soon. Do you have any more queries? (yes/no)"

    elif conversation_state["stage"] == "post_lead":
        if text == "yes":
            conversation_state["stage"] = "start"
            return "Sure! Ask me anything about pricing or plans."
        else:
            conversation_state["stage"] = "done"
            return "Thank you! Have a great day."

    if text in ["no", "nope", "not interested"]:
        conversation_state["stage"] = "done"
        return "No problem! Thank you for your time."

    intent = detect_intent(user_input)

    if intent == "greeting":
        return "Hello! Ask me about pricing or plans."
    elif intent == "pricing":
        return rag_response(user_input)
    elif intent == "high_intent":
        conversation_state["stage"] = "ask_name"
        return "Great! What's your name?"

    return "Please ask about pricing, plans, or policies."

# Chat loop
while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = agent(user)
    print("Bot:", response)

    if conversation_state["stage"] == "done":
        break