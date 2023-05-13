from flask import Flask, jsonify, request
app = Flask(__name__)
List = [
    {'id':1,
        'Name':'RAJU',
        'Contact':'9999999999',
        'done':False
    },
    {
        'id':2,
        'Name':'Juice',
        'Contact':'8888888888',
        'done':False
    },
    {
        'id':3,
        "Name":'Gerald',
        'Contact':'7777777777',
        'done':False
    }]
@app.route("/")
def helloworld():

    return "hello World"
@app.route("/add-data",method=["POST"])

def add_task():
    
    if not request.json:
        return jsonify({
    "status":"error",
    "message":"please provide the data"

        }, 400)
    contact={
        'id':'task'[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',"")
    }
    List.append(contact)
@app.route("/get-data")
def getData():
    return jsonify({
        'data':List
    })
if (__name__=="__main__"):
    app.run(debug=True)