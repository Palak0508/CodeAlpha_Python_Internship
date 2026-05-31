def run_chatbot():
    print("Task 4: Basic Chatbot")
    print("Type 'quit' to end the conversation.")
    
    while True:
        user_message = input("\nYou: ").lower().strip()
        
        if user_message == "quit":
            print("Chatbot: Goodbye. Have a great day.")
            break
            
        if "hello" in user_message or "hi" in user_message:
            print("Chatbot: Hello. How can I help you today?")
        elif "your name" in user_message:
            print("Chatbot: I am a simple Python chatbot created for this internship.")
        elif "how are you" in user_message:
            print("Chatbot: I am functioning perfectly. Thank you for asking.")
        elif "python" in user_message:
            print("Chatbot: Python is a powerful and easy-to-learn programming language.")
        elif "weather" in user_message:
            print("Chatbot: I cannot check live weather data right now, but I hope it is pleasant where you are.")
        elif "help" in user_message:
            print("Chatbot: You can ask me about Python, my name, or say hello.")
        else:
            print("Chatbot: I do not understand that phrase. Could you try asking something else?")

if __name__ == "__main__":
    run_chatbot()