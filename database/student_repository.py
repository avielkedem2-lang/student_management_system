from database.db_management import DBConnector
from fastapi import HTTPException

class StudentsDB:
    def __init__(self):
        self.db = DBConnector()
    
    def create_table(self):
        try:
            self.db.connect()
            self.db.cursor.execute("""create table if not exists students (
                                    id int primary key,
                                    name varchar(50) not null,
                                    age int not null,
                                    course varchar(100) not null,
                                    status varchar(20) default 'active',
                                    email varchar(150) unique);""")
        except Exception as e:
            return e

        finally:
            self.db.cursor.close()
    

    def create_student(self, body):
        self.db.connect()
        try:
            body = dict(body)
            if not body.get("status"):
                body["status"] = "active"
            self.db.cursor.execute("insert into students(id, name, age, course, status, email) values (%s, %s, %s, %s, %s, %s)",
                                (body["id"], body["name"], body["age"], body["course"], body["status"], body["email"]))
            self.db.connection.commit()
            return {"seuccess": True}
        except Exception as e:
            raise HTTPException(409, f"{e}")

        finally:
            self.db.cursor.close()

    def get_all_students(self):
        try:
            self.db.connect()
            self.db.cursor.execute("select * from students")
            return self.db.cursor.fetchall()
        except Exception as e:
            print(e)
    
        finally:
            self.db.cursor.close()


    def get_student_by_id(self,id):
        try:
            self.db.connect()
            self.db.cursor.execute("select * from students where id=%s", (id,))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
    
        finally:
            self.db.cursor.close()


    def update_name_by_id(self,new_name, id):
        try:
            self.db.connect()
            self.db.cursor.execute("update students set name=%s where id=%s",(new_name, id))
            self.db.connection.commit()
            return self.db.cursor.rowcount
        except Exception as e:
            print(e)
    
        finally:
            self.db.cursor.close()
    

    def delete_student_by_id(self, id):
        try:
            self.db.connect()
            self.db.cursor.execute("delete from students where id=%s", (id,))
            self.db.connection.commit()
            return self.db.cursor.rowcount
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()


    def count_students(self):
        try:
            self.db.connect()
            self.db.cursor.execute("select count(*) as total_students from students")
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)