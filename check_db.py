from app import app, Product, VendorRestock

with app.app_context():
    # Query and print all products
    products = Product.query.all()
    print("\nProducts in database:")
    for product in products:
        print(f"- {product.brand} {product.model} ({product.type}) - ${product.price}")