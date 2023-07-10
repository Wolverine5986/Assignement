# import all required libraries
from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from bson import ObjectId
from bson.json_util import dumps
import CONFIG as path

# flask object
app = Flask(__name__)
app.secret_key = "secret_key"

## configure Mongo database
app.config['MONGO_URI'] = 'mongodb://localhost:27017/User'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'yash'

# Add user user URL
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    # id = data['id']
    name = data['name']
    email = data['email']
    password = data['password']
    if request.method == 'POST':
        mongo.db.user.insert_one({'name':name,'email':email,'password':password})
        result = jsonify('user created')
        return result
    else:
        return "Something Went Wrong"
    
## Display all users from database
@app.route('/users')
def users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp

# fetch user from database by using id
@app.route('/users/<id>')
def user(id):
    user = mongo.db.user.find_one({'_id':ObjectId(id)})
    result = dumps(user)
    return result

## delete user by there id
@app.route('/delete/<id>',methods=['DELETE'])
def delete_user(id):
    user = mongo.db.user.delete_one({'_id':ObjectId(id)})
    result = jsonify('deleted')
    return result

## Update data by id
@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    data = request.json
    name = data['name']
    email= data['email']
    password =  data['password']

    if request.method =='PUT':
        mongo.db.user.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                                 {'$set':{'name':name,'email':email, 'password':password}})        
        result = jsonify('updated')
        return result
    else:
        return "Something Went Wrong"


if __name__ == '__main__':
    app.run(debug = True, port=path.port, host=path.host)

