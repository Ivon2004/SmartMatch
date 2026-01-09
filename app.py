from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils.helpers import find_phone_matches, get_suggested_searches
from data.mock_data import mock_data

app = Flask(__name__)
app.secret_key = 'smartmatch_secret_key'
app.config['DEBUG'] = True

# Database configuration (SQLite)
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "smartmatch.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Product {self.brand} {self.model}>"


class VendorRestock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    brands = sorted(list(mock_data.keys()))
    return render_template('index.html', brands=brands)

@app.route('/search', methods=['POST'])
def search():
    brand = request.form.get('brand', '')
    model = request.form.get('model', '')
    product_type = request.form.get('type', '')  # Get product type from form
    
    # Use enhanced search from helpers with product type filter
    results = find_phone_matches(brand, model, mock_data, product_type='cover' if 'cover' in model.lower() else None)
    
    # If no exact matches, get suggestions
    suggestions = []
    if not results:
        suggestions = get_suggested_searches(model, mock_data)
    
    return render_template('results.html',
                         results=results,
                         brand=brand,
                         model=model,
                         suggestions=suggestions)

@app.route('/restock')
def restock():
    """Display the restock list from session"""
    restock_items = session.get('restock_list', [])
    total_price = sum(item.get('price', 0) * item.get('quantity', 1) for item in restock_items)
    return render_template('restock.html', 
                         restock_items=restock_items,
                         total_price=total_price)

@app.route('/add_to_restock', methods=['POST'])
def add_to_restock():
    """Add item to restock list"""
    brand = request.form.get('brand', '')
    model = request.form.get('model', '')
    product_type = request.form.get('type', '')
    price = float(request.form.get('price', 0))
    quantity = int(request.form.get('quantity', 1))
    
    if 'restock_list' not in session:
        session['restock_list'] = []
    
    # Add item to restock list
    item = {
        'brand': brand,
        'model': model,
        'type': product_type,
        'price': price,
        'quantity': quantity
    }
    session['restock_list'].append(item)
    session.modified = True
    
    return redirect(url_for('restock'))

@app.route('/remove_from_restock', methods=['POST'])
def remove_from_restock():
    """Remove item from restock list"""
    index = int(request.form.get('index', 0))
    
    if 'restock_list' in session:
        if 0 <= index < len(session['restock_list']):
            session['restock_list'].pop(index)
            session.modified = True
    
    return redirect(url_for('restock'))

if __name__ == '__main__':
    print("Server starting... Access the application at:")
    print("http://127.0.0.1:5000 or http://localhost:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
