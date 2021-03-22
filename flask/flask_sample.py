import os
from flask import Flask, url_for

app = Flask(__name__, static_folder='.', static_url_path='')

# ルーティング
@app.route("/hello")
def hello_world():
    return "Hello world"

@app.route("/user/<username>")
def show_user_profile(username):
    return "UserName: " + str(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post" + str(post_id)

@app.route('/')
def index():
    return url_for("show_user_profile", username="ai_academy")
 
@app.route('/hello/<name>')
def hello(name):
    return name

if __name__ == "__main__":
    app.run(port=8000, debug=True)