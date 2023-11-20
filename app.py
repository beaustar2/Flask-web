# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>Hello there!</h1>
    <p>Welcome to my aspiring journey as a DevOps Engineer. I'm currently a work in progress, but hey, aren't we all?</p>
    <p>Feel free to explore this space and discover the exciting things I'm building on my way to becoming a seasoned DevOps pro!</p>
    <p>Stay tuned for more updates and happy coding!</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0')