from flask import Flask, jsonify, send_from_directory
import app

flask_app = Flask(__name__)

@flask_app.route('/')
def root():
    return flask_app.send_static_file('index.html')

@flask_app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return flask_app.send_static_file(path)

@flask_app.route('/api')
def greeting():
    return jsonify({"app": "interest profiler"})

@flask_app.route('/api/favorites/<twitter_username>', methods=['GET'])
def get_favorites(twitter_username):
    favorites = app.get_favorites(twitter_username)
    return jsonify(favorites)

@flask_app.route('/api/interests/<twitter_username>', methods=['GET'])
def get_interests(twitter_username):
    interests = app.user_interests(twitter_username)
    return jsonify(interests)

if __name__ == "__main__":
    flask_app.run(host='127.0.0.1', port=8080, debug=True)
