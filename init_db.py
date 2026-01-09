from app import db, app, Product, VendorRestock
from data.mock_data import mock_data

def init_db():
    with app.app_context():
        # Create all database tables
        db.create_all()
        print("Created database tables")

        # Check if we already have products
        if Product.query.first() is None:
            # Convert mock_data to database entries
            for brand, items in mock_data.items():
                for item in items:
                    product = Product(
                        brand=brand,
                        model=item['model'],
                        type=item['type'],
                        price=float(item['price']),
                        image=item.get('image', None)
                    )
                    db.session.add(product)
            
            # Commit the changes
            db.session.commit()
            print("Added sample products to database")
        else:
            print("Database already contains products")

if __name__ == '__main__':
    print("Initializing database...")
    init_db()
    print("Database initialization complete!")
    
    # Print some stats
    with app.app_context():
        product_count = Product.query.count()
        restock_count = VendorRestock.query.count()
        print(f"\nDatabase contains:")
        print(f"- {product_count} products")
        print(f"- {restock_count} restock items")