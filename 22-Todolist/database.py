import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("/home/ete/Public/codes/00ME/PyLearn/22-Todolist/TodoList.db")
        self.cursor = self.con.cursor()
    

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    def get_tasks_done(self):
        query = "SELECT * FROM done_tasks"
        result = self.cursor.execute(query)
        done_tasks = result.fetchall()
        return done_tasks

    
    def add_new_task(self, new_title, new_desc, time_str, new_priority):
        try:
            query = f"INSERT INTO tasks (title, description, time, priority) VALUES('{new_title}', '{new_desc}', '{time_str}', '{new_priority}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
    

    def remove_task(self, task_id):
        try:
            query = f"DELETE FROM tasks WHERE id={task_id}"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def task_done(self, task_id):
        try:
            query = f"INSERT INTO done_tasks (id, title, description, time) SELECT id, title, description, time FROM tasks WHERE id={task_id}"
            self.cursor.execute(query)
            
            # After adding to done, remove from tasks
            self.remove_task(task_id)
            
            self.con.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

