import psycopg2


class Database:

  host = 'localhost'
  database = 'admin'
  user = 'admin'
  password = 'admin'

  def __init__(self):

    host = self.host
    database = self.database
    user = self.user
    password = self.password
    self.conn = psycopg2.connect(host=str(self.host), database=str(self.database),
                                 user=str(self.user), password=str(self.password))
    self.cursor = self.conn.cursor()

  def close(self):
    return self.conn.close()

  def query(self, query_string):

    self.cursor.execute(query_string)
    return_object = self.cursor.fetchall()
    return return_object

  def insert(self, query_string, data):
    self.cursor.execute(query_string, data)
    self.conn.commit()

  def create_table(self, query_string):
    self.cursor.execute(query_string)
    self.conn.commit()
    return print("table created")

  def update_table(self, query_update, query_data):
    self.cursor.execute(query_update, query_data)
    self.conn.commit()
    return print("updated table")
