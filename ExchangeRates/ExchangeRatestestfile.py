# Name : Robin Garg
# Roll No : 2019092
# Group : 2

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		self.assertAlmostEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 0.014,delta=0.0005)
		self.assertEqual(changeBase(3, "EUR", "USD", "1999-08-15"), 3.2001)
		self.assertAlmostEqual(changeBase(5, "INR", "GBP", "2010-10-25"), 0.01, delta = 0.1)
		self.assertAlmostEqual(changeBase(7, "USD", "MYR", "2015-07-15"), 26.6, delta = 0.05)
		self.assertEqual(changeBase(1, "EUR", "INR", "2019-03-11"), 78.547)
		self.assertEqual(changeBase(1.3965, "CAD", "TRY", "2017-02-11"), 3.9173)
		self.assertAlmostEqual(changeBase(3.1, "PLN", "JPY", "2000-02-29"), 82.09, delta= 0.001)
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.




if __name__=='__main__':
	unittest.main()
