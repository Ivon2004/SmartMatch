# SmartMatch

SmartMatch is a Python-based system designed to match users efficiently using structured logic and database support.
## Project Title:
SmartMatch – Smart Accessory Locator System
## Overview:
SmartMatch is a digital system designed to help phone accessory vendors quickly locate and identify covers and screen protectors for their customers. The platform provides a visual catalog that allows vendors to search by phone brand or model and instantly view matching product images.
## Problem Statement:
Vendors often spend too much time searching for specific accessories when customers request them. Sorting through unorganized stock slows down service, reduces efficiency, and can lead to missed sales opportunities.
## Proposed Solution:
SmartMatch simplifies the search process by providing an intelligent catalog of phone accessories. When a vendor searches for a phone model, the system displays corresponding images of available covers and screen protectors. Vendors can easily confirm stock availability or add unavailable items to a Restock Page for future replenishment. (Ordering from suppliers is not part of the system.)
## Project Structure
app.py # Main application entry point
create_db.py # Creates the database
init_db.py # Initializes database tables/data
check_db.py # Verifies database integrity
smartmatch.db # SQLite database file

markdown
Copy code

## Technologies Used
- **Python**
- **SQLite**

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/ivon2004/SmartMatch.git
Navigate into the project directory:

bash
Copy code
cd SmartMatch
Run the application:

bash
Copy code
python app.py
Ensure Python is installed on your system before running the project.

## Features
Database creation and initialization

Data validation and checking

Modular Python scripts for maintainability

Simple backend logic flow

## Use Case
SmartMatch can serve as:

A backend learning project

A foundation for building a web or mobile application

A demonstration of database-driven Python logic

## Future Improvements
Add a web interface (Flask/FastAPI)

User authentication and roles

API endpoints

Cloud deployment

Improved matching algorithms

## Author
Ivon Mitchel
Backend & Systems Development Learner
