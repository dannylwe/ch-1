users = []

def create_user(username):
	users.append(username)
	return

def create_todolist(username, todolist_name):
	if username in users:
		list(todolist_name)
		global todo_name
		todo_name = todolist_name.copy()

		global todo 

		todo = {
		"username": username,
		"todolist_name": todolist_name,
		}

		return todo_name

def create_task(user_name, todolist_name, task_description):
	create_user(username)
	create_todolist(username, todolist_name)
	todo_name.append(task_description)
	return

def remove_user(user_name):
	users.remove(user_name)
	return

def remove_task_from_list(todolist_name, task):
	todolist_name.remove(task)
	return

def remove_all_tasks(todolist_name):
	for x in todolist_name:
		todolist_name.remove(x)
	return

def get_user_tasks(user_name, no_of_tasks):
	if user_name in todo['username']:
		return len(todo['todolist_name'])

def get_user_tasks(user_name, task_no):
	if user_name in todo['username']:
		find_list= todo['todolist_name']
		return find_list[task_no]
