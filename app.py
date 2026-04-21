from flask import Flask, request, jsonify, render_template
from groq import Groq
 
app = Flask(__name__)
client = Groq()
 
history = []
 
@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    history.append({"role": "user", "content": user_message})
 
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )
 
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
 
    return jsonify({"reply": reply})
 
if __name__ == "__main__":
    app.run(debug=True)