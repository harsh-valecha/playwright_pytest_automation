import os
import sqlite3

class Config:
    appointment_url = 'https://katalon-demo-cura.herokuapp.com/'
    login_url = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    book_appointment_url = 'https://katalon-demo-cura.herokuapp.com/#appointment'

    @staticmethod
    def get_users():
        db_path = os.path.join(os.path.dirname(__file__), 'katalondb.sqlite')
        conn = sqlite3.connect(db_path)
        cursor = conn.execute('select * from users')
        credentials = []
        for row in cursor:
            credentials.append({'username': row[1], 'password': row[2]})
        conn.close()
        return credentials


#print(Config.get_users())