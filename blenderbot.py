# /Users/chris/build_chatbot_for_your_data/LLM_application_chatbot/blenderbot.py
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class BlenderBot:
    def __init__(self, model_name="facebook/blenderbot-400M-distill"):
        self.model_name = model_name
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.conversation_history = []

    def get_response(self, user_input):
        # Create conversation history string
        history = "\n".join(self.conversation_history)

        # Tokenize the input text and history
        inputs = self.tokenizer.encode_plus(history, user_input, return_tensors="pt")

        # Generate the response from the model
        outputs = self.model.generate(**inputs, max_length=60)

        # Decode the response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Add interaction to conversation history
        self.conversation_history.append(user_input)
        self.conversation_history.append(response)

        return response
