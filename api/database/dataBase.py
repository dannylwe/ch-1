import psycopg2
from psycopg2.extras import RealDictCursor
import os

class Database:

	host = 'ec2-23-21-201-12.compute-1.amazonaws.com'
	database = 'd1c3rnkp9oer5r'
	user = 'tqhmdglqvqqbqt'
	password = 'd7db46e743f2ef535cc07bd74ff36d288c8832df121fb515a30b95911642b06f'

	def __init__(self):

		host = self.host
		database = self.database
		user = self.user
		password = self.password
		self.conn = psycopg2.connect(host=str(self.host), database=str(self.database),
		user= str(self.user), password=str(self.password))
		self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

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

	def teardown(self):
		self.cursor.execute("DROP table parcel, users;")
		self.conn.commit()
		return print("\tteardown complete")


db = Database()
db.create_table()

