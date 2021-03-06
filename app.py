import os
from flask import Flask, render_template, redirect, session, request, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
import re
from datetime import date
from bson import Binary, Code, json_util
from bson.json_util import dumps, loads
import json
from os import path
if path.exists("env.py"):
  import env 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)
app.secret_key = os.environ.get('SECRET_KEY')


# rating recipe based on user's stars
def rating(rate1, rate2, rate3, rate4, rate5):
    score = rate1+2*rate2+3*rate3+4*rate4+5*rate5
    num_raters = rate1+rate2+rate3+rate4+rate5
    if num_raters == 0:
        return 0
    return score / num_raters


@app.route('/')
@app.route('/find_recipe')
def find_recipe():
    recipes=mongo.db.recipes.find().sort("recipe_date", -1)
    return render_template("find_recipe.html", recipes=recipes)


@app.route('/sign_in', methods=["POST", "GET"])
def sign_in():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form.get('username')})
        if login_user:
            if request.form.get('pass') == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for("find_recipe"))
        return render_template('sign_in.html', invalid_pass=True)
    return render_template('sign_in.html')


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one(
            {'username': request.form.get('username')})
        if request.form.get('pass') != request.form.get('pass2'):
            return render_template('sign_up.html', invalid_pass=True)
        if existing_user is None:
            users.insert({'username': request.form.get(
                'username'), 'password': request.form.get('pass'), 'rated_recipes':[]})
            session['username'] = request.form['username']
            return redirect(url_for('find_recipe'))
        return render_template('sign_up.html', invalid_username=True)
    return render_template('sign_up.html')


@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
                           users=mongo.db.users.find(), active_user=session['username'])


@app.route('/add_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    if 'recipe_photo' in request.files:
        
        recipe_photo=request.files['recipe_photo']
        mongo.save_file(recipe_photo.filename, recipe_photo)
        recipes.insert_one(
            {
        'recipe_meal':request.form.get('recipe_meal'),
        'recipe_name':request.form.get('recipe_name'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe': request.form.get('recipe'),
        'recipe_energy':request.form.get('recipe_energy'),
        'recipe_photo':recipe_photo.filename,
        'recipe_video':request.form.get('recipe_video'),
        'recipe_username':request.form.get('recipe_username'),
        'recipe_date':request.form.get('recipe_date'),
        'recipe_rate1':0,
        'recipe_rate2':0,
        'recipe_rate3':0,
        'recipe_rate4':0,
        'recipe_rate5':0        
        })
    else:
        recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_recipe'))


@app.route('/photo/<photoname>')
def photo(photoname):
    return mongo.send_file(photoname)


@app.route('/search_recipe', methods=['POST', 'GET'])
def search_recipe():
    recipes = mongo.db.recipes
    # creating index
    recipes.create_index([('recipe_meal', 'text'), ('recipe_name', 'text'), ('recipe', 'text'),
                          ('recipe_ingredients', 'text'), ('recipe_energy', 'text')],name="search_index", weights={'title': 100, 'body': 25})
    SR = recipes.find({'$text': {'$search': request.form.get('search_recipe')}})
    if SR:
        return render_template("search_recipe.html",
                           recipes_search=SR, recipes=mongo.db.recipes.find())
    else:
        return render_template("search_recipe.html",
                           recipes_search=SR, recipes=mongo.db.recipes.find(), no_recipe=True)


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session['username']=[]
    return redirect(url_for('find_recipe'))


@app.route('/my_recipe')
def my_recipe():
    return render_template("my_recipe.html",
                           my_recipes=mongo.db.recipes.find({"recipe_username": session['username']}))


@app.route('/one_my_recipe/<recipe_id>')
def one_my_recipe(recipe_id):
    recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('one_my_recipe.html', recipe=recipe)


@app.route('/one_recipe/<recipe_id>', methods=['POST', 'GET'])
def one_recipe(recipe_id):
    recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    user_in=[]
    if session:
        user_in=mongo.db.users.find_one({"username": session['username']})
    rate=rating(recipe['recipe_rate1'], recipe['recipe_rate2'], recipe['recipe_rate3'], recipe['recipe_rate4'], recipe['recipe_rate5'])    
    return render_template('one_recipe.html', recipe=recipe, user_in=user_in, rate=rate, id=str(recipe["_id"]))


@app.route('/rate_recipe/<recipe_id>', methods=['POST', 'GET'])
def rate_recipe(recipe_id):
    users = mongo.db.users
    recipes = mongo.db.recipes
    if request.form.get('recipe_rate11'):
        users.update({'username': session['username']}, {'$push': {'rated_recipes': recipe_id}})
        recipes.update({'_id': ObjectId(recipe_id)}, {'$inc': {'recipe_rate1': 1}})
    if request.form.get('recipe_rate22'):
        users.update({'username': session['username']}, {'$push': {'rated_recipes': recipe_id}})
        recipes.update({'_id': ObjectId(recipe_id)}, {'$inc': {'recipe_rate2': 1}})
    if request.form.get('recipe_rate33'):
        users.update({'username': session['username']}, {'$push': {'rated_recipes': recipe_id}})
        recipes.update({'_id': ObjectId(recipe_id)}, {'$inc': {'recipe_rate3': 1}})
    if request.form.get('recipe_rate44'):
        users.update({'username': session['username']}, {'$push': {'rated_recipes': recipe_id}})
        recipes.update({'_id': ObjectId(recipe_id)}, {'$inc': {'recipe_rate4': 1}})
    if request.form.get('recipe_rate55'):
        users.update({'username': session['username']}, {'$push': {'rated_recipes': recipe_id}})
        recipes.update({'_id': ObjectId(recipe_id)}, {'$inc': {'recipe_rate5': 1}})
    return redirect(url_for('one_recipe', recipe_id=recipe_id))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html', user_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}))


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    users_c = mongo.db.users
    users = mongo.db.users.find()
    rater=[]
    for user in users:
        if str(recipe_id) in user['rated_recipes']:
            rater = user['username']
        users_c.update({'username': rater}, {'$pull': {'rated_recipes': recipe_id}})
    if 'recipe_photo' in request.files:        
        recipe_photo=request.files['recipe_photo']
        mongo.save_file(recipe_photo.filename+'new', recipe_photo)
        recipes.update( {'_id': ObjectId(recipe_id)},
        {
        'recipe_meal':request.form.get('recipe_meal'),
        'recipe_name':request.form.get('recipe_name'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe': request.form.get('recipe'),
        'recipe_energy':request.form.get('recipe_energy'),
        'recipe_photo':recipe_photo.filename,        
        'recipe_username':request.form.get('recipe_username'),
        'recipe_date':request.form.get('recipe_date'),
        'recipe_rate1':0,
        'recipe_rate2':0,
        'recipe_rate3':0,
        'recipe_rate4':0,
        'recipe_rate5':0
        })    
    else:
        recipes.update_many( {'_id': ObjectId(recipe_id)},
        {
        'recipe_meal':request.form.get('recipe_meal'),
        'recipe_name':request.form.get('recipe_name'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe': request.form.get('recipe'),
        'recipe_energy':request.form.get('recipe_energy'),
        'recipe_username':request.form.get('recipe_username'),
        'recipe_date':request.form.get('recipe_date'),
        'recipe_rate1':0,
        'recipe_rate2':0,
        'recipe_rate3':0,
        'recipe_rate4':0,
        'recipe_rate5':0
        })
    print(request.form.get('recipe_date'))
    return redirect(url_for('my_recipe'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipe'))


# sending active_user to all htmls
@app.context_processor
def inject_user():
    if session:
        return dict(active_user=session['username'])
    else:
        return dict()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
