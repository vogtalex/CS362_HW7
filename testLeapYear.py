import unittest
import leapYear

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(leapYear.leapYearChecker(4), "Yes")
		self.assertEqual(leapYear.leapYearChecker(100), "No")



if __name__ == '__main__':
	unittest.main()