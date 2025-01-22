def chatbot():
    print("Hello! I'm ChatBot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello! How can I help you today?")

        elif "how are you" in user_input:
            print("ChatBot: I'm just a program, but I'm functioning as expected! How about you?")

        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot, your virtual assistant.")

        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"ChatBot: The current time is {current_time}.")

        elif "weather" in user_input:
            print("ChatBot: I can't fetch the weather right now, but it's always a good idea to check your local weather app!")

        elif "help" in user_input:
            print("ChatBot: I'm here to help! You can ask me about the time, weather, or just say hi.")

        else:
            print("ChatBot: I'm sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
