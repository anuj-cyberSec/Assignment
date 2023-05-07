from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    prompt = request.form["prompt"]
    response = chat(prompt)
    return render_template("results.html", prompt=prompt, response=response)

def chat(prompt):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    data = {
        "prompt": f"Conversation with a user:\nUser: {prompt}\nAI:",
        "max_tokens": 1024,
        "temperature": 0.7,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",  # Replace with your API key
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return f"Error: {response.text}"

