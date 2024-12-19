from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Base for models
Base = declarative_base()

# Define Department model
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)
    employees = relationship("Employee", back_populates="department")


# Define Employee model
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    position = Column(String)
    salary = Column(Float)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")


# Create the database engine
engine = create_engine("sqlite:///db.sqlite3")

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()
