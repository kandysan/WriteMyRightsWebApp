import mysql.connector
db_conn = mysql.connector.connect(host="localhost", user="root", password="P@ssw0rd", database="WMRdb")
db_cursor = db_conn.cursor()


# must change address to geo location later
db_cursor.execute('''
          CREATE TABLE users
          (id INT NOT NULL AUTO_INCREMENT, 
           name VARCHAR(250) NOT NULL,
           geo_location VARCHAR(250) NOT NULL,
           email VARCHAR(250) NOT NULL,
           date_created VARCHAR(100) NOT NULL,
           CONSTRAINT users_pk PRIMARY KEY (id))
          ''')

db_conn.commit()
db_conn.close()
