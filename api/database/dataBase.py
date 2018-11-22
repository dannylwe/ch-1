import psycopg2
import os

# conn = psycopg2.connect(host="localhost",database="admin", user="admin", password="admin")

# cur = conn.cursor()

# #cur.execute("CREATE TABLE test(id serial PRIMARY KEY, name varchar, email varchar)")
# cur.execute("SELECT * FROM playground;")
# items = cur.fetchall()

# for item in items:
# 	print(item)

# # print(items)

# conn.commit()
# cur.close()
# conn.close()

#create a setup function to create tables and run them in run.py

class Database:

	host = 'localhost'
	database = 'admin'
	user = 'admin'
	password = 'admin'

	def __init__(self):

		# if os.getenv('TESING_DB')== 'testing':
		# 	database= '####'
		#export TESTING_DB=testing

		host = self.host
		database = self.database
		user = self.user
		password = self.password
		self.conn = psycopg2.connect(host=str(self.host), database=str(self.database),
		user= str(self.user), password=str(self.password))
		self.cursor = self.conn.cursor()

	def query(self, query_string):
		self.cursor.execute(query_string)
		return_object = self.cursor.fetchall()
		return return_object

	def insert(self, query_string, data):
		self.cursor.execute(query_string, data)
		self.conn.commit()

	def create_table(self):
		query_table_create= """CREATE TABLE IF NOT EXISTS users (user_id SERIAL,
 		email VARCHAR(30), password VARCHAR(20), handphone INTEGER, username VARCHAR(16),
 		admin BOOLEAN DEFAULT False, PRIMARY KEY (username)); CREATE TABLE IF NOT EXISTS parcel (parcel_id SERIAL, 
		nickname VARCHAR(20), pickup VARCHAR(40), destination VARCHAR(40), 
		weight INTEGER, status VARCHAR(20) DEFAULT 'pending', order_time date, username VARCHAR(20),
 		FOREIGN KEY (username) REFERENCES users (username));"""
		self.cursor.execute(query_table_create)
		self.conn.commit()
		
#remove try and except for teardown 

	def teardown(self):
		self.cursor.execute("DROP table parcel, users;")
		self.conn.commit()
		return print("\tteardown complete")


db = Database()
try:
	db.teardown()
except e:
	print(e)
db.create_table()


	# def update_table(self, query_update, query_data):
	# 	self.cursor.execute(query_update, query_data)
	# 	self.conn.commit()
	# 	return print("updated table")

	
	 	# self.cursor.execute(create_parcel_table)
	 	# self.conn.commit()

	 	# return "success"




	# def __delete__(self):
	# 	self.conn.commit()
	# 	self.cursor.close()
	# 	self.conn.close()
		

# if __name__ == '__main__':

# 	db = Database()
# 	query = "SELECT * FROM playground;"
# 	#db.query(query)

# create_user_table = """CREATE TABLE IF NOT EXISTS users (user_id SERIAL,
#  email VARCHAR(30), password VARCHAR(20), handphone INTEGER, username VARCHAR(16),
#  admin BOOLEAN DEFAULT False, PRIMARY KEY (username));"""

# create_parcel_table = """CREATE TABLE IF NOT EXISTS parcel (parcel_id SERIAL, 
# nickname VARCHAR(20), pickup VARCHAR(40), destination VARCHAR(40), 
# weight INTEGER, status VARCHAR(20) DEFAULT 'pending', order_time date, username VARCHAR(20),
#  FOREIGN KEY (username) REFERENCES users (username));"""

# admin_priv= update users set admin=True where username= 'danny1';

# 	# get_one = """SELECT * FROM playground LIMIT 1;"""
# 	# print(db.query_one(get_one))
# 	query_2 = """INSERT INTO USERS (email, password, handphone, username) VALUES (%s,
# 	%s, %s, %s)"""
# 	query_2_insert = ('danny@gmail.com', 'ggg', 1224, 'gghfh')

# 	query_update = """UPDATE USERS set email = %s, password = %s""" 
# 	query_data = ('hello@gmail.com', '123password')

# 	for item in db.query(query):
# 		print(item)

# 	db.create_table(instance_database)
# 	db.insert(query_2, query_2_insert)
# 	db.update_table(query_update, query_data)

#psql -V 9.5

