import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-kuifg.mongodb.net/cookbook?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
@app.route('/find_recipe')
def find_recipe():
    return render_template("find_recipe.html", 
                           users=mongo.db.users.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", 
                           users=mongo.db.users.find())


@app.route('/sign_in')
def sign_in():
    return render_template("sign_in.html", 
                           users=mongo.db.users.find())


@app.route('/sign_up')
def sign_up():
    return render_template("sign_up.html", 
                           users=mongo.db.users.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','5000')),
            debug=True)
