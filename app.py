import os
from flask import Flask, render_template, redirect, session, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-kuifg.mongodb.net/cookbook?retryWrites=true&w=majority"
mongo = PyMongo(app)

app.secret_key = "randomstring123"


@app.route('/')
@app.route('/sign_in', methods=["POST", "GET"])
def sign_in():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form.get('username')})
        if login_user:
            if request.form.get('pass') == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for("find_recipe"))
        return 'Invalid username/password combination'
    return render_template('sign_in.html')


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one(
            {'username': request.form.get('username')})

        if existing_user is None:
            users.insert({'username': request.form.get(
                'username'), 'password': request.form.get('pass')})
            session['username'] = request.form['username']
            return redirect(url_for('find_recipe'))

        return 'That username already exists!'

    return render_template('sign_up.html')


# I should ask how the hell is working????????
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
                           users=mongo.db.users.find(), active_user=session['username'])


@app.route('/add_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('find_recipe'))


@app.route('/find_recipe')
def find_recipe():
    return render_template("find_recipe.html",
                           recipes=mongo.db.recipes.find(), active_user=session['username'])


@app.route('/find_recipe', methods=['POST', 'GET'])
def search_recipe():
    recipes = mongo.db.recipes
    recipes.ensure_index([('recipe_name', 'text'), ('recipe', 'text')],
                         name="search_index", weights={'title': 100, 'body': 25})

# recipes.ensure_index([('recipe_name', 'text'), ('recipe', 'text'), ('recipe_meal', 'text'), ('recipe_ingredients', 'text')
#     , ('recipe_energy', 'text'), ('recipe_photo', 'text'), ('recipe_video', 'text'),], name="search_index", weights={'title':100,'body':25})

    SR = recipes.find(
        {'$text': {'$search': request.form.get('search_recipe')}})

    

    return render_template("find_recipe.html",
                           recipes_search=SR, recipes=mongo.db.recipes.find(), active_user=session['username'])


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
