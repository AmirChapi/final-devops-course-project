from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # להרצה מקומית בלי דוקר (אופציונלי)
    app.run(host="0.0.0.0", port=5000)
