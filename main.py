# import all required libraries
from flask import Flask,jsonify,request, render_template, redirect,url_for
from flask_pymongo import PyMongo
from bson import ObjectId
from app.utils import application
import app.CONFIG as path

util = application()

# flask object
app = Flask(__name__)
app.secret_key = path.SECREAT_KEY

## configure Mongo database
app.config['MONGO_URI'] = path.DATABASE_PATh # Mongo db connection with collection
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('add.html')

# Add user user URL
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        data = request.form
        user = util.add_user(data)
        mongo.db.user.insert_one(user)
        msg = util.add
        return render_template('add.html',msg=msg)
    else:
        return render_template('add.html')
    
## Display all users from database
@app.route('/users')
def users():
    users = mongo.db.user.find()
    result = users
    return render_template('users.html' ,result=result)

## delete user by there id
@app.route('/delete/<id>',methods=['GET','DELETE'])
def delete(id):
    mongo.db.user.delete_one({'_id':ObjectId(id)})
    msg = util.delete
    return redirect(url_for('users',msg=msg))

## Update data by id
@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    if request.method == "POST":
        data = request.form
        name = data['name']
        email= data['email']
        password =  data['password']
        mongo.db.user.update_one({'_id':ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)},{'$set':{'name':name,'email':email, 'password':password}})
        msg = util.update        
        return redirect(url_for('users',msg=msg))
    else:
        user = mongo.db.user.find_one({'_id':ObjectId(id)})
        return render_template('update.html', user = user)
if __name__ == '__main__':
    app.run(debug = True)

