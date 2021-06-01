import unittest
import fizzBuzz

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(fizzBuzz.printFizz(1), 1)
		self.assertEqual(fizzBuzz.printFizz(3), "Fizz")
		self.assertEqual(fizzBuzz.printFizz(5), "Buzz")




if __name__ == '__main__':
	unittest.main()