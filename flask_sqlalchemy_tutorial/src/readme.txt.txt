$python3 (or pythyon) -m venv .

go into the Scripts directory and activate
$. activate --> remember the .

$python
>> from dbtest import db
>> from dbtest import User
>> andrew = User(username='andrew', email='andrew@test.com')
>> admin = User(username='admin', email='admin@test.com')
>> db.session.add(andrew)
>> db.session.add(admin)
>> db.session.commit()

# verify
# User.query.all()


# turn off venv
$ deactivate