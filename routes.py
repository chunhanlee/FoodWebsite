from flask import Blueprint, render_template, request, session
from flask_session import Session
from models import get_categoryList, get_foodList, get_categoryName, User, get_food

bp = Blueprint('food', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/intro')
def intro():
    return render_template('intro.html')

@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.get_by_username(username)
    if user and user.password == password:
        session['user_id'] = user.id
        return 'Logged in successfully'
    return 'Invalid credentials', 401

# @bp.route('/<int:food_id>')
# def details(food_id):
#     food = FoodInfo.query.get_or_404(food_id)
#     return render_template('details.html', food=food)

@bp.route('/foodcategories')
def food_categories():
    foodCategories = get_categoryList()
    return render_template('foodcategories.html', foodCategories=foodCategories)



    # conn = get_db_connection()
    # foodCategories = conn.execute('SELECT * FROM Food_Category').fetchall()
    # conn.close()
    # return render_template('foodcategories.html', foodCategories=foodCategories)

@bp.route('/foodcategories/foods/<int:category_id>')
def food_by_categories(category_id):
    foods = get_foodList(category_id)
    category_name = get_categoryName(category_id)
    return render_template('foods.html', foods=foods, category_name=category_name.name)

# @app.route('/foodcategories/foods/<int:category_id>')
# def food_by_categories(category_id):
#     foods = get_foodList(category_id)
#     category_name = get_CategoryName(category_id)
#     return render_template('foods.html', foods=foods, category_name=category_name['name'])

@bp.route('/foodcategories/foods/<int:category_id>/<int:food_id>')
def fooddetails(category_id,food_id):
    food = get_food(food_id)
    return render_template('foodDetails.html', food=food)

# @app.route('/foodcategories/foods/<int:category_id>/<int:food_id>')
# def fooddetails(category_id,food_id):
#     food = get_food(food_id)
#     return render_template('foodDetails.html', food=food)