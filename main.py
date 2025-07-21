user_input = input("User:")
responses = {
    "hello": "Hi There!",
    "How Are You": "I am Good, Thank You!",
    "What is your name?": "I am Chatbot",
    "Default": "Sorry, I did not understand that."
}
ai_response = responses.get(user_input.lower(), responses["Default"])
print("AI:",ai_response)