delivered_orders= [3, 6, 9, 12]
pending =[1, 2, 4, 8, 10]

def check_order_status(order_id):
	if order_id in delivered_orders:
		return True
	else:
		return False

def check_pending(order_id):
	if order_id in pending:
		return True
	else:
		return False

def new_order(order_id):
	return delivered_orders.append(order_id)

def flag_delivered(order_id):
	flag = pending.pop(pending.index(order_id))
	return delivered_orders.append(flag)

def check_pending_empty():
	if len(pending) > 0:
		return False
	else:
		return True

def check_delivered_empty():
	if len(delivered_orders) > 0:
		return False
	else:
		return True
