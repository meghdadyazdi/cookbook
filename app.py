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
@app.route('/find_recipe')
def find_recipe():
    if session:
        return render_template("find_recipe.html",
                           recipes=mongo.db.recipes.find(), active_user=session['username'])
    else:
        return render_template("find_recipe.html",
                           recipes=mongo.db.recipes.find())

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
        # return 'Invalid username/password combination'
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
        return render_template('sign_up.html', invalid_username=True)
        # return 'That username already exists!'

    return render_template('sign_up.html')


# I should ask how the hell is working????????
@app.route('/add_recipe')
def add_recipe():
    # return render_template("add_recipe.html",
    #                        users=mongo.db.users.find(), active_user=session['username'])
    return render_template("add_recipe.html",
                           users=mongo.db.users.find(), active_user=session['username'])


@app.route('/add_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_recipe'))


@app.route('/search_recipe', methods=['POST', 'GET'])
def search_recipe():
    recipes = mongo.db.recipes
    # recipes.ensure_index([('recipe_name', 'text'), ('recipe', 'text')],
    #                      name="search_index", weights={'title': 100, 'body': 25})

    recipes.create_index([('recipe_meal', 'text'), ('recipe_name', 'text'), ('recipe', 'text'),
                          ('recipe_ingredients', 'text'), ('recipe_energy', 'text')],name="search_index", weights={'title': 100, 'body': 25})

# recipes.ensure_index([('recipe_name', 'text'), ('recipe', 'text'), ('recipe_meal', 'text'), ('recipe_ingredients', 'text')
#     , ('recipe_energy', 'text'), ('recipe_photo', 'text'), ('recipe_video', 'text'),], name="search_index", weights={'title':100,'body':25})
    SR = recipes.find({'$text': {'$search': request.form.get('search_recipe')}})

    if SR:
        return render_template("search_recipe.html",
                           recipes_search=SR, recipes=mongo.db.recipes.find(), active_user=session['username'])
    else:
        return render_template("search_recipe.html",
                           recipes_search=SR, recipes=mongo.db.recipes.find(), active_user=session['username'], no_recipe=True)


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session['username']=[]
    return redirect(url_for('find_recipe'))

@app.route('/my_recipe')
def my_recipe():
    return render_template("my_recipe.html",
                           my_recipes=mongo.db.recipes.find({"recipe_username": session['username']}), active_user=session['username'])






@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html', user_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}),
                                          recipes=mongo.db.recipes.find(),
                                          active_user=session['username'])


@app.route('/update_recipe/<recipe_id>', methods=['POST', 'GET'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_meal':request.form.get('recipe_meal'),
        'recipe_name':request.form.get('recipe_name'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe': request.form.get('recipe'),
        'recipe_energy':request.form.get('recipe_energy'),
        'recipe_photo':request.form.get('recipe_photo'),
        'recipe_video':request.form.get('recipe_video'),
        'recipe_username':request.form.get('recipe_username')
    })
    return redirect(url_for('my_recipe'))




@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipe'))

















if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
