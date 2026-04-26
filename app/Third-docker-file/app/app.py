import os
from flask import Flask

app = Flask(__name__)

ENV = os.getenv("ENV", "dev")

@app.route("/")
def home():
    return f"🚀 App running in {ENV} environment!"

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
