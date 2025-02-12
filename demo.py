from flask import Flask, jsonify, request
import gradio as gr
from blenderbot import BlenderBot  # Import your chatbot class or function

app = Flask(__name__)
chatbot = BlenderBot()  # Initialize Blender chatbot

# Flask route for API endpoint (optional)
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    bot_response = chatbot.get_response(user_input)
    return jsonify({"response": bot_response})

# Gradio Interface
def chatbot_interface(user_input):
    return chatbot.get_response(user_input)

interface = gr.Interface(
    fn=chatbot_interface,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="BlenderBot Chatbot",
    description="A chatbot powered by BlenderBot.",
)

# Flask and Gradio integration
@app.route("/")
def gradio_ui():
    return interface.launch(server_name="0.0.0.0", server_port=8080, share=False, prevent_thread_lock=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)