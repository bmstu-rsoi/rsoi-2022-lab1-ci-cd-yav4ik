import psycopg2

DB_URL = 'postgres://stwmuuojohnnxb:fc2eb6d8a87c2d1c6c28834d2f1ee89a79261fe1195b9693411890a8cb3600f4@ec2-52-211-233' \
         '-176.eu-west-1.compute.amazonaws.com:5432/dbnndfrngm61gm'


class DatabaseRequests:
    def __init__(self):
        self.DB_URL = DB_URL

        if not self.check_persons_tabele():
            self.create_table()

    def check_persons_tabele(self):
        db = psycopg2.connect(self.DB_URL, sslmode="require")
        sql = db.cursor()
        sql.execute("""SELECT table_name FROM information_schema.tables
               WHERE table_schema = 'public'""")
        for table in sql.fetchall():
            if table[0] == "persons":
                sql.close()
                return True
        sql.close()
        db.close()
        return False

    def create_table(self):
        new_table = '''
                    CREATE TABLE persons
                    (
                    person_id serial not null,
                       name varchar,
                       address varchar,
                       work varchar,
                       age varchar
                    );

                    CREATE unique index persons_person_id_uindex
                       on persons (person_id);

                    alter table persons
                       add constraint persons_pk
                           primary key (person_id);
                    '''
        db = psycopg2.connect(self.DB_URL, sslmode="require")
        cursor = db.cursor()
        cursor.execute(new_table)
        db.commit()
        cursor.close()
        db.close()

    def get_person(self, person_id):
        db = psycopg2.connect(self.DB_URL, sslmode="require")
        cursor = db.cursor()
        cursor.execute(f"SELECT * From persons WHERE person_id={person_id};")
        person = cursor.fetchone()
        cursor.close()
        db.close()
        return person

    def get_all_persons(self):
        db = psycopg2.connect(self.DB_URL, sslmode="require")
        cursor = db.cursor()
        cursor.execute(f"SELECT * From persons;")
        persons = cursor.fetchall()
        cursor.close()
        db.close()
        return persons

    def add_person(self, new_info):
        db = psycopg2.connect(self.DB_URL, sslmode="require")
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO persons (person_id, name, address, work, age) VALUES (DEFAULT, '{new_info['name']}', "
                       f"'{new_info['address']}', '{new_info['work']}', '{new_info['age']}') RETURNING person_id;")
        db.commit()
        person_id = cursor.fetchone()
        cursor.close()
        db.close()
        return person_id[0]

    def update_person(self, new_info, person_id):
        db = psycopg2.connect(self.DB_URL, sslmode="require")
        cursor = db.cursor()
        cursor.execute(f"UPDATE persons SET name = '{new_info['name']}', address = '{new_info['address']}', "
                       f"work = '{new_info['work']}', age = '{new_info['age']}' "
                       f"WHERE person_id={person_id};")
        db.commit()
        cursor.close()
        db.close()

    def delete_person(self, person_id):
        db = psycopg2.connect(self.DB_URL, sslmode="require")
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM persons WHERE person_id={person_id};")
        db.commit()
        cursor.close()
        db.close()



