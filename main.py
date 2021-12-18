from flask import Flask, jsonify
from random import randint
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)


def random_likes():
    return [randint(1, 10) for _ in range(48)]


@app.route("/likes")
def root():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    response = {d: random_likes() for d in days}
    response["days"] = days
    return jsonify(response)


if __name__ == "__main__":
    app.run()
