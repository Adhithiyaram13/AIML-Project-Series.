import random


class AdmissionBot:
    def __init__(self):
        self.user_context = {}

    def get_response(self, user_input):
        user_input = user_input.lower()

        if "reset" in user_input:
            self.user_context = {}
            return "Sure, let's start over. How can I help you with your college admission?"

        if "admission procedures" in user_input:
            response = "To start the admission process, you need to fill out the online application form on our website. Do you have specific questions about the application form?"
            self.user_context['topic'] = 'admission_procedures'
            return response

        if "admission requirements" in user_input:
            response = "Admission requirements include academic transcripts, recommendation letters, and a personal statement. Have you gathered all the necessary documents?"
            self.user_context['topic'] = 'admission_requirements'
            return response

        if "deadlines" in user_input:
            response = "The admission deadlines vary for different programs. Please visit our website or contact the admissions office for the most accurate and up-to-date information."
            self.user_context['topic'] = 'admission_deadlines'
            return response

        if 'topic' in self.user_context:
            return self.handle_follow_up(user_input)

        if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
            return "Hello! How can I assist you with your college admission today?"

        return "I'm sorry, but I couldn't understand that. Could you please rephrase or ask another question?"

    def handle_follow_up(self, user_input):
        topic = self.user_context['topic']

        if topic == 'admission_procedures':
            if "application form" in user_input:
                return "The application form is available on our website. You can also find step-by-step instructions on how to complete it."

        elif topic == 'admission_requirements':
            if "documents" in user_input:
                return "Make sure you have your academic transcripts, recommendation letters, and a well-crafted personal statement. If you have specific questions about any document, feel free to ask."

        elif topic == 'admission_deadlines':
            return "For program-specific deadlines, please check the information on our official website or contact the admissions office."

        return "I'm sorry, I couldn't provide a specific answer to that follow-up question. If you have another question, feel free to ask."


admission_bot = AdmissionBot()

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break

    response = admission_bot.get_response(user_input)
    print("Bot:", response)
