from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Mess Optimizer is Running!"

if __name__ == "__main__":
    app.run()
