# CooKBooK

Food lovers around the world are looking for new recipes everyday. This application is designed to help them find new and old recipes for known and unknown 
foods. User can also share his/her own recipe. 

You can find a live demo [here](https://cookbook-meghdad.herokuapp.com/)
 
## UX
CookBooK website is designed for general users who wants to have a quick search in recipes and for a little bit more serious users who like to share their recipes.
 
## User stories
As a user:
- You will search recipe name, ingredients, energy level, ... to find recipes.
- You will sing up to website to be able to add your own (or others) recipes to share it with other users
- You can edit or delete your recipes.
- All the users who are signed in can give star (Excelent, Very good, Good, Average and Bad) to all recipes to rate them. Users give stars to recipes and then they can see how a recipe is rated from one to five stars.

### Structure
In the home page all the recipes are sorted by the date they are added or edited. Recent recipes are at the top. All visitors can see all the recipes and the rate for each recipe.
But to add, edit, or give star to recipes visitors should sign in or if they have not signed up yet the should sign up first.

### Design
Recipes are shown in the home page in a clickable card to go to the full recipe page.

## Technologies

### HTML5  

### CSS

### Materialize CSS
 - Google materialize is the main tool to design and structure the ellements on the pages. The resnponsive navbar, sid bar and footers are all desiged using Materialize. 

### JQuery
 - With JQuery is used for dropdown menu and side bar. The clickabale rating stars which shows and counts the rates of recipes are all controlled ne JQuery.

### Python

### Heroku
- The application is deployed to Heroku.

### Flask
- To make routes in Python and render or redirect them.

### MongoDB
- All the data related to recipes and users are stor in MongoDB.
  * Two collections are created. RECIPES collection for storing all recipes data (recipe_name, recipe_ingredients, recipe_energy, recipe_photo, recipe_username and recipe_rate). USERS for storing data related to
    users (username, password and rated_recipes)

### Pymongo
- To make a connection between MongoDB database and Python.

### Jinja
- To make a Python-like expressions in HTML. 

### Font Awesome
- Some of the icons are from Font Awesome.

### Material Icons
- Some of the icons are from Material Icons.

## Features Left to Implement
The search will be improved in such a way that by typing part of the searched keyword all suggested keyword are shown.
The sorting will be based on recipe rating too.
Users can comment on the recipes.
User can have chat with owner of a recipe.

## Testing
In test.py file all the routs and rating(a1, a2, a3, a4, a5) are tested. 

The sign in and sign up are tested. If users enter a invalid username or password there will be short notice.
To sign up, the password should be repeated with the same password. If users enter diffrent passwords there will be again a short notice.

Every user can rate a recipe just once but when the recipe is edited, rates will be removed and all users can rate it again. This issue was tested to make sure that user 
can rate a recipe once.

While developing the code I realized that session is not removed and I developed the code while I was not aware of that. So when I opened the aplication in a new browser or in incognito window
there was an error alarming "No username found". I decided to run the app always in incognito widow to be aware of changes in session.

The application was tested on Chrome and FireFox and different devices like mobile (iPhone and Samsung) and iPads to check the responsiveness.

## Deployment
This application is deployed to Heroku and the following *config vars* are add properly:
- IP 
- PORT
- MONGO_URI
- SECRET_KEY

The application is also pushed to my Github repository `https://github.com/meghdadyazdi/cookbook` which can be cloned

## Content
All content in this application were written by me.

## Acknowledgements
I solved a lot of my problems during development of this application by the help of [StackOverflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) websites.
