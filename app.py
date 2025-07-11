from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("https://webhook.site/dbe4edad-666e-4b5a-badf-424f4b3a4e09", code=302)

if __name__ == "__main__":
    app.run(debug=True)
