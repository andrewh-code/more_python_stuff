from model import db, User
from sqlalchemy import text


if __name__ == "__main__":
    db.create_all()

    # insert
    insert_stmt = text('insert into user (username, email) values(\'andrew\', \'andrew@test.com\')')
    insert_stmt2 = text('insert into user (username, email) values(\'andrew2\', \'andrew2@test.com\')')

    result = db.session.execute(insert_stmt)
    result = db.session.execute(insert_stmt2)
    db.session.commit()

    # select staement
    select = text('select * from user')
    users = db.session.execute(select)

    # delete
    delete = text('delete from user where username=\'andrew2\'')
    delete_result = db.session.execute(delete)
    db.session.commit()
    
    users = db.session.execute(select)
    for user in users:
        print(user)



