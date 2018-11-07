import unittest
from check_order import (check_order_status, check_pending, new_order, 
	delivered_orders, flag_delivered, check_pending_empty, check_delivered_empty)

class TestOrders(unittest.TestCase):

	def test_check_order(self):
		return self.assertEqual(check_order_status(3), True)
	"""
	def test_check_int(self):
		self.assertRaises(ValueError, check_order_status, "3")
	"""

	def tetst_check_int(self):
		self.assertFalse(check_order_status("3"))

	def test_not_in_both(self):
		self.assertFalse(check_order_status(-1))

	def test_in_pending(self):
		self.assertEqual(check_pending(2), True)

	def test_new_order(self):
		x = new_order(16)
		self.assertIn(16, delivered_orders)

	def test_marked_to_deliver(self):
		y= flag_delivered(10)
		self.assertIn(10, delivered_orders)

	def test_check_pending_empty(self):
		self.assertEqual(check_pending_empty(), False)

	def test_check_delivered_empty(self):
		self.assertEqual(check_delivered_empty(), False)