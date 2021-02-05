import sqlite3

conn = sqlite3.connect('surveys.sqlite')

c = conn.cursor()

c.execute('''
          CREATE TABLE employment_answers
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(250) NOT NULL,
           company_name VARCHAR(250) NOT NULL,
           boss_name VARCHAR(250) NOT NULL,
           time_worked VARCHAR(250) NOT NULL,
           severance VARCHAR(250) NOT NULL,
           email VARCHAR(250) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

conn.commit()
conn.close()
