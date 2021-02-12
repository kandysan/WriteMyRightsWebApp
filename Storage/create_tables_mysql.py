import mysql.connector
db_conn = mysql.connector.connect(host="localhost", user="root", password="P@ssw0rd", database="events")
db_cursor = db_conn.cursor()

db_cursor.execute('''
          CREATE TABLE employment_answers
          (id INT NOT NULL AUTO_INCREMENT, 
           name VARCHAR(250) NOT NULL,
           address VARCHAR(250) NOT NULL,
           company_name VARCHAR(250) NOT NULL,
           company_address VARCHAR(250) NOT NULL,
           boss_name VARCHAR(250) NOT NULL,
           time_worked VARCHAR(250) NOT NULL,
           severance VARCHAR(250) NOT NULL,
           email VARCHAR(250) NOT NULL,
           date_created VARCHAR(100) NOT NULL,
           CONSTRAINT pickup_pk PRIMARY KEY (id))
          ''')

db_conn.commit()
db_conn.close()
