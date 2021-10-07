from flask import Flask
from flask import jsonify
from flask_cors import CORS

import random


app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return jsonify({'name': 'Jimit',
                    'address': 'India'})


@app.route('/get_user/', methods=['GET', 'POST'])
def get_user():
    return jsonify({'name': 'Vijit',
                    'email': 'shrivastav@gmail.com'})


@app.route('/get_sales/', methods=['GET', 'POST'])
def get_sales():
    sales = [{'month': 'Jan',
             'value': '10'},
             {'month': 'Feb',
             'value': '15'},
             {'month': 'March',
             'value': '5'},
             {'month': 'April',
             'value': '2'},
             {'month': 'May',
             'value': '55'}]
    return jsonify(sales)


@app.route('/get_profits/', methods=['GET', 'POST'])
def get_profits():
    randomlist = []
    for i in range(0, 5):
        n = random.randint(1, 30)
        randomlist.append(n*2)
    print(randomlist)
    return jsonify(randomlist)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
