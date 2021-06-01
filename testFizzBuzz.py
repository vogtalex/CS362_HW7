import unittest
import fizzBuzz

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(fizzBuzz.printFizz(1), 1)




if __name__ == '__main__':
	unittest.main()