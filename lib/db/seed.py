import sys
import os

# Ensure the root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from lib.db.models import session, Department, Employee

def seed_database():
    print("Seeding the database with sample data...")

    # Create Departments
    departments = [
        Department(name="HR", location="Mombasa"),
        Department(name="Engineering", location="Konza City"),
        Department(name="Marketing", location="Nairobi"),
        Department(name="Sales", location="Nakuru"),
        Department(name="IT", location="Remote"),
    ]

    # Add departments
    session.add_all(departments)
    session.commit()
    print("Departments added!")

    # Create Employees
    employees = [
        Employee(first_name="John", last_name="Dee", email="john@gmail.com", phone="0715251252",
                position="HR Manager", salary=90000, department=departments[0]),
        
        Employee(first_name="Jane", last_name="Smith", email="jane.smith@gmail.com", phone="0752524565",
                position="Software Engineer", salary=120000, department=departments[1]),
        
        Employee(first_name="Robert", last_name="Brown", email="robert.brown@gmail.com", phone="078565425",
                position="Marketing Specialist", salary=85000, department=departments[2]),

        Employee(first_name="Emily", last_name="Davis", email="emily.davis@gmail.com", phone="0741255612",
                position="Sales Executive", salary=95000, department=departments[3]),

        Employee(first_name="Michael", last_name="Johnson", email="michael.johnson@gmail.com", phone="0756854525",
                position="IT Support Specialist", salary=80000, department=departments[4]),

        Employee(first_name="Sara", last_name="Lee", email="sara.lee@gmail.com.com", phone="0745251525",
                position="Product Manager", salary=150000, department=departments[1]),

        Employee(first_name="David", last_name="Wilson", email="david.wilson@gmail.com", phone="0745258695",
                position="Sales Manager", salary=110000, department=departments[3]),
        
        Employee(first_name="Laura", last_name="Taylor", email="laura.taylor@gmail.com", phone="0745258545",
                position="Data Analyst", salary=95000, department=departments[2]),
    ]

    # Add employees
    session.add_all(employees)
    session.commit()
    print("Employees added successfully!")


if __name__ == "__main__":
    seed_database()
