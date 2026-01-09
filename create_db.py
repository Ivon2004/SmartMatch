from app import db, app

if __name__ == '__main__':
    # Use application context so SQLAlchemy can access app configuration
    with app.app_context():
        db.create_all()
        print('Database created (smartmatch.db)')
