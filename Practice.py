def simple_ai():
    print("Hello! I'm a simple AI. You can chat with me (type 'quit' to exit)")
    
    # Dictionary of predefined responses
    responses = {
        "hello": "Hi there! How are you?",
        "how are you": "I'm doing well, thank you for asking!",
        "what is your name": "My name is SimpleAI!",
        "bye": "Goodbye! Have a great day!",
        "help": "I can respond to basic greetings and questions. Try saying 'hello' or asking 'what is your name'",
    }
    
    while True:
        # Get user input and convert to lowercase
        user_input = input("You: ").lower().strip()
        
        # Check if user wants to quit
        if user_input == 'quit':
            print("AI: Goodbye!")
            break
        
        # Look for matching response
        response_found = False
        for key in responses:
            if key in user_input:
                print("AI:", responses[key])
                response_found = True
                break
        
        # Default response if no match found
        if not response_found:
            print("AI: I'm not sure how to respond to that. Try asking something else!")

if __name__ == "__main__":
    simple_ai()
