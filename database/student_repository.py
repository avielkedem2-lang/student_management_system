from database.db_management import DBConnector


class StudentsDB:
    def __init__(self):
        self.db = DBConnector()
    
    def create_table(self):
        self.db.connect()
        try:
            self.db.cursor.execute("""create table if not exists students (
                                   id int auto_increment primary key,
                                   name varchar(50) not null,
                                   age int not null,
                                   course varcher(100) not null,
                                   status varchar(20) default 'active',
                                   email varchar(150) unique);""")
        except Exception as e:
            return e