from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return "<Employee(id='%s', first_name='%s', last_name='%s', email='%s')>" % (
            self.id, self.first_name, self.last_name, self.email)


class Employee2(db.Model):
    __tablename__ = 'employee2'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    department = db.relationship("Department", uselist=False, back_populates="employee2")
    
    def __repr__(self):
        return "<Employee2(first_name='%s', last_name='%s', email='%s', department='%s')>" % (
            self.first_name, self.last_name, self.email, self.department.id)

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    employee2_id = db.Column(db.Integer, db.ForeignKey('employee2.id'))
    department_name = db.Column(db.String(100), unique=False, nullable=False)
    employee2 = db.relationship("Employee2", back_populates="department")
    
    def __repr__(self):
        return "<Department: \n id \t |\t employee2_id |\t  department_name | \n '%s'\t |'%s' \t '%s'|" % (
            self.id, self.employee2_id, self.department_name)
        

        