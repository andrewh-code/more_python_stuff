from model import db, Employee, Employee2, Department
import sys

def create_employees():
    
    list_employee = []

    new_employee = Employee(first_name="test",
                            last_name="employee",
                            email="test@test.com")
    list_employee.append(new_employee)
    
    new_employee = Employee(first_name="test2",
                            last_name="employee2",
                            email="test2@test.com")
    list_employee.append(new_employee)

    new_employee = Employee(first_name="test3",
                            last_name="employee3",
                            email="test3@test.com")
    list_employee.append(new_employee)

    new_employee = Employee(first_name="test4",
                            last_name="employee4",
                            email="test4@test.com")
    list_employee.append(new_employee)

    return list_employee


def populate_employee_table(db):
    
    employees = create_employees()
    for employee in employees:
        db.session.add(employee)
    db.session.commit()


def create_employee2_with_department(db):
    
    new_emp2 = Employee2(first_name="em",
                          last_name="last", 
                          email="email@email.com")
    db.session.add(new_emp2)
    db.session.commit()

    # department = Department(Employee2(first_name="em", last_name="last", email="email@email.com"), department_name="dev")
    department = Department(employee2=new_emp2, department_name="dev")
    db.session.add(department)
    db.session.commit()

    # print (db.session.query(new_emp2))
    for d in db.session.query(Department):
        print(d)

if __name__ == "__main__":
    db.create_all()
    # populate_employee_table(db)
    
    create_employee2_with_department(db)
    
    # Employee.query.all()
    for e in db.session.query(Employee):
        print(e)

    for e in db.session.query(Employee):
        if e.first_name == "test2":
            db.session.delete(e)
    
    for e in db.session.query(Employee):
        print(e)
    
    


