from os.path import join, dirname
from hashlib import sha256
from sqlite3 import connect, OperationalError, IntegrityError


class Hash:
    def __init__(self):
        self.db_obj = join(dirname(__file__), 'demo.sqlite')
        self.set = connect(self.db_obj)
        self.crs = self.set.cursor()

    def create_table(self):
        create_statemt = 'CREATE TABLE user_info (user_login qwerty(255)' \
                        'unigue, user_password qwerty(255)'
        try:
            self.crs.execute(create_statemt)
        except OperationalError:
            print('Table already exists')
        else:
            self.set.commit()
            print('Table added successfully')

    @staticmethod
    def give_hash():
        login = input('Enter your login: ')
        pswd = input('Enter your password: ')
        hash_ob = sha256(login.encode() + pswd.encode()).hexdigest()
        return login, hash_ob

    def registration(self):
        login, re_hash = self.give_hash()
        check_statemt = 'INSERT INTO user_info (user_login, user_password' \
                        'VALUES (?, ?)'
        user_info = (login, re_hash)
        try:
            self.crs.execute(check_statemt, user_info)
        except IntegrityError:
            print('The entry exists. Sign in')
        else:
            self.set.commit()
            print('Registration completed')

    def login(self):
        login, chech_hach = self.give_hash()
        select_statemt = 'SELECT user_password FROM user_info WHERE user_login = ?'
        self.crs.execute(select_statemt, (login))
        ex_hash = self.crs.fetchone()
        if chech_hach == ex_hash[0]:
            print('Welcome')
        else:
            print('Re-enter the password. Or register')

network = Hash()
network.create_table()
network.registration()
network.login()



