from model import db, Exercise
from sqlalchemy import text
import csv
import sys

def create_insert_stmt(exercise_name, exercise_type, muscle_group, youtube_link):
    str_insert = "insert into exercise (exercise_name, exercise_type, muscle_group, youtube_link) values ('{}', '{}', '{}', '{}')".format(exercise_name, exercise_type, muscle_group, youtube_link)
    print(str_insert)
    return text(str_insert)

if __name__ == "__main__":
    db.create_all()
    del_char = ','
    num_columns = 4
    
    # select
    select = "select * from exercise"

    with open('exercise.csv', 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=del_char)
        row_count = 0;        
        for row in csv_reader:
            row_count = row_count + 1
            if len(row) != 4:
                print("row: %s does not have the same number of columnns: %s" % (row_count, num_columns))
                sys.exit()
            sql_insert = create_insert_stmt(row[0], row[1], row[2], row[3])
            
            db.session.execute(sql_insert)

    
    db.session.commit()

    exercises = db.session.execute(select)
    print(exercises.keys())
    for exercise in exercises:
        print(exercise)