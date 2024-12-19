
# **📊 Company Employee Tracker CLI App**

A command-line application built using **Python**, **SQLAlchemy**, and **SQLite** to manage company departments and employees. It supports CRUD operations such as adding, updating, viewing, and deleting records.

---

## **📁 Project Structure**
```
company-employee-tracker/
│── alembic.ini         # Alembic configuration file
│── db.sqlite3          # SQLite database
│── migrations/         # Database migrations
│── lib/
│   ├── __init__.py     # Project initialization
│   ├── cli.py          # Main CLI script
│   └── db/
│       ├── __init__.py # Database initialization
│       ├── models.py   # SQLAlchemy models
│       ├── seed.py     # Data seeding script
│── README.md           # Project documentation
```

---

## **🔧 Features**
- **Department Management:**
  - Add, View, Update, and Delete Departments
- **Employee Management:**
  - Hire, View, Update, and Remove Employees
  - View Employees by Department
  - List All Employees

---

## **🚀 How to Run the Project**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/company-employee-tracker.git
cd company-employee-tracker
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Database Migrations**
```bash
alembic upgrade head
```

### **5. Seed the Database**
```bash
python lib/db/seed.py
```

### **6. Run the Application**
```bash
python lib/cli.py
```

---

## **📋 Example Commands**

1. **Run the CLI App:**
   ```bash
   python lib/cli.py
   ```

2. **Add a Department Example:**
   ```
   Choose an option: 1
   Enter department name: Engineering
   Enter location: Remote
   Department added successfully!
   ```

3. **View All Employees:**
   ```
   Choose an option: 5
   ID: 1, Name: John Doe, Position: Developer, Department: IT
   ```

---

## **📚 Built With**
- **Python 3.x** - Programming Language
- **SQLAlchemy** - ORM for managing the database
- **SQLite3** - Lightweight database
- **Alembic** - Database migrations

---

## **📂 Database Models**
### **Departments Table**
| Field Name  | Data Type  | Description         |
|-------------|-------------|---------------------|
| id          | Integer    | Primary Key         |
| name        | String     | Department Name     |
| location    | String     | Department Location |

### **Employees Table**
| Field Name     | Data Type  | Description              |
|----------------|-------------|--------------------------|
| id             | Integer    | Primary Key              |
| first_name     | String     | Employee First Name      |
| last_name      | String     | Employee Last Name       |
| email          | String     | Employee Email           |
| phone          | String     | Employee Phone Number    |
| position       | String     | Employee Job Title       |
| salary         | Float      | Employee Salary          |
| department_id  | Integer    | Foreign Key (Departments)|

---

## **📂 Project Management Commands**
| Command                     | Description                  |
|----------------------------|------------------------------|
| `python lib/cli.py`         | Run the CLI App             |
| `python lib/db/seed.py`     | Seed the Database           |
| `alembic revision`          | Create DB Migrations        |
| `alembic upgrade head`      | Apply DB Migrations         |
| `sqlite3 db.sqlite3`        | Open the Database in CLI    |

---

## **🔧 Contributing**
If you'd like to contribute, please fork the repository and submit a pull request.

---

## **⚠️ License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **🙌 Acknowledgments**
- SQLite
- SQLAlchemy
- Python CLI Best Practices

---

Let me know if you need anything else added! 🚀