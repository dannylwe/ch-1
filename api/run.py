from views.app import app

# def setup():
# 	db = Database()

# 	create_parcel_table = """CREATE TABLE IF NOT EXISTS parcel (parcel_id SERIAL PRIMARY KEY,
# 	user_id INTEGER, nickname VARCHAR(20), pickup VARCHAR(40), destination VARCHAR(40), weight INTEGER, 
# 	status VARCHAR(20) DEFAULT 'pending', order_time date, FOREIGN KEY(user_id) REFRENCES users (user_id))"""

# 	create_user_table = """CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, 
# 	email VARCHAR(30), password VARCHAR(20), handphone INTEGER, username VARCHAR(16))"""

#  	db.create_table(create_user_table)
#  	db.create_table(create_parcel_table)

# setsup = setup()




 	


if __name__ == '__main__':
	app.run()
	# setsup()
	