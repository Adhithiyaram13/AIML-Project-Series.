import random


class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I assist you today?"

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask anytime."

    def respond_to_question(self, question):
        if "weather" in question.lower():
            return "I'm sorry, I don't have information about the weather right now."
        elif "name" in question.lower() or "who are you" in question.lower():
            user_name = self.context.get("What's your name?", "")
            if user_name:
                return f"Hi {user_name}! Nice to meet you."
            else:
                return "I'm just a simple chatbot, you can call me ChatGPT. What's your name?"
        elif "how are you" in question.lower():
            return "I'm just a computer program, so I don't have feelings, but thanks for asking!"
        elif "programming" in question.lower():
            return "I can help you with basic programming questions. What language are you interested in?"
        elif "age" in question.lower():
            return "I don't have an age. I'm here to assist you with any questions you have."
        elif "hello" in question.lower():
            return "Hello! I'm glad to see you. What brings you here?"

        # Handle user's responses
        elif "favorite color" in question.lower():
            user_color = self.context.get(
                "What's your favorite color?", "").lower()
            if user_color:
                return f"That's a great choice! {user_color} is a wonderful color."
            else:
                return "I see. What's your favorite color?"
        elif "pets" in question.lower():
            user_pets = self.context.get("Do you have any pets?", "").lower()
            if user_pets:
                return f"Ah, {user_pets}! Pets are wonderful companions."
            else:
                return "Interesting. Do you have any pets?"
        elif "day going" in question.lower():
            return "I hope your day is going well! Anything exciting happening?"
        elif "favorite type of music" in question.lower():
            user_music = self.context.get(
                "What's your favorite type of music?", "").lower()
            if user_music:
                return f"Nice choice! I also enjoy listening to {user_music}."
            else:
                return "Cool! What's your favorite type of music?"
        elif "good movies lately" in question.lower():
            return "I'm just a chatbot, so I don't watch movies, but I'd love to hear your recommendations."
        else:
            return None

    def ask_user_questions(self):
        questions = ["What's your name?", "What's your favorite color?", "Do you have any pets?",
                     "How's your day going?", "What's your favorite type of music?",
                     "Have you seen any good movies lately?", "How can I help you today?",
                     "Do you have any specific questions in mind?"]
        user_responses = {}

        for question in questions:
            user_input = input(question + " ")
            user_responses[question] = user_input

        return user_responses

    def handle_user_responses(self, user_responses):
        self.context.update(user_responses)

    def chat(self):
        print(self.greet())

        for _ in range(1):
            user_responses = self.ask_user_questions()
            self.handle_user_responses(user_responses)

        print("Great! Let's chat with the information you provided.")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "bye":
                print(self.farewell())
                break

            response = self.respond_to_question(user_input)
            if response:
                print("Chatbot:", response)
            else:
                print(
                    "Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

        print(self.farewell())


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
