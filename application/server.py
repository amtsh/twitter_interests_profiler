from flask import Flask, jsonify
app = Flask(__name__)
app.debug = True

@app.route("/")
def greeting():
    return jsonify({"app": "interest profiler"})

def world():
    return jsonify("Hello")

if __name__ == "__main__":
    app.run()
