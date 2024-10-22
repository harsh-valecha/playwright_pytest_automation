import os
import sqlite3

class Config:
    appointment_url = 'https://katalon-demo-cura.herokuapp.com/'
    login_url = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    book_appointment_url = 'https://katalon-demo-cura.herokuapp.com/#appointment'
    summary_url = 'https://katalon-demo-cura.herokuapp.com/appointment.php#summary'
    dynamic_element_url = 'https://the-internet.herokuapp.com/dynamic_loading/1'
    jquery_ui_url = 'https://the-internet.herokuapp.com/jqueryui/menu#'

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

    @staticmethod
    def get_form_data():
        db_path = os.path.join(os.path.dirname(__file__), 'katalondb.sqlite')
        conn = sqlite3.connect(db_path)
        cursor = conn.execute('''select users.username , users.password , form_data.facility , 
        form_data.apply_for_hospital_readmission , form_data.healthcare_program , 
        strftime('%d/%m/%Y', form_data.visit_date ), form_data.comment 
        from users cross join form_data ;''')
        data = []
        for row in cursor:
            data.append({'username': row[0], 'password': row[1],'facility':row[2],
                                'apply_for_hospital_readmission':row[3],'healthcare_program':row[4],
                                'visit_date':row[5],'comment':row[6]})
            # print(row)
        conn.close()
        return data

#print(Config.get_users())
print(Config.get_form_data())