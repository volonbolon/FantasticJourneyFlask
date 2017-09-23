from flask import Flask
from flask import abort
from flask import request
from flask import make_response
from flask import jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def homepage():
    time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

@app.route('/locations', methods=['POST'])
def locations():
    payload = request.get_json()

    print(payload)
    print(app.name)

    locations = mongo.db.locations
    try:
        locations.insert_one(payload)
        success = True
        status_code = 201
    except:
        success = False
        status_code = 400

    response = jsonify({"success":success})
    response.status_code = status_code

    return response

if __name__ == '__main__':
    app.run(debug=True)
