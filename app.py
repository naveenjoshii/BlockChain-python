from Blockchain import Blockchain
from flask import Flask,jsonify,render_template,request,redirect,url_for
import json
app = Flask(__name__)

bc = Blockchain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['nm']
        b = bc.addBlock(name)
        print("================================")
        print("=New node added to Blockchain!!=")
        print("================================")
    return redirect(url_for('get_chain'))


# Display blockchain in json format
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = []

    for i in bc.chain:
        d = {"timestamp": i.timestamp,
        "hash":i.hash,
        "lastHash" :i.lastHash,
        "data" : i.data,
        "nonce" : i.nonce,
        "difficulty" : i.difficulty
        }
        response.append(d)
    return render_template('index.html',response = response)



app.run()
