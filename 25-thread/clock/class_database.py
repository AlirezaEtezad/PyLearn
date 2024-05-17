import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("alarm.db")
        self.cursor = self.con.cursor()
    

    def get_alarms(self):
        query = "SELECT * FROM alarms"
        result = self.cursor.execute(query)
        alarms = result.fetchall()
        return alarms
    

    
    def add_new_alarm(self, new_title, time_str):
        try:
            query = f"INSERT INTO alarms (title, time) VALUES('{new_title}', '{time_str}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
    

    def remove_alarm(self, alarm_id):
        try:
            query = f"DELETE FROM alarms WHERE id={alarm_id}"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

