import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_food(food_id):
    conn = get_db_connection()
    food = conn.execute('SELECT * FROM FoodInfo WHERE id = ?', (food_id,)).fetchone()
    conn.close
    if food is None:
        abort(404)
    return food

def get_foodList(category_id):
    conn = get_db_connection()
    foods = conn.execute('SELECT * FROM FoodInfo WHERE category_id = ?', (category_id,)).fetchall()
    conn.close
    if foods is None:
        abort(404)
    return foods

def get_CategoryName(category_id):
    conn = get_db_connection()
    name = conn.execute('SELECT name FROM Food_Category WHERE id = ?', (category_id,)).fetchone()
    conn.close
    if name is None:
        abort(404)
    return name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/foodcategories')
def food_categories():
    conn = get_db_connection()
    foodCategories = conn.execute('SELECT * FROM Food_Category').fetchall()
    conn.close()
    return render_template('foodcategories.html', foodCategories=foodCategories)

@app.route('/foodcategories/foods/<int:category_id>')
def food_by_categories(category_id):
    foods = get_foodList(category_id)
    category_name = get_CategoryName(category_id)
    return render_template('foods.html', foods=foods, category_name=category_name['name'])

@app.route('/foodcategories/foods/<int:category_id>/<int:food_id>')
def fooddetails(category_id,food_id):
    food = get_food(food_id)
    return render_template('foodDetails.html', food=food)
