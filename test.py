import unittest
import example

class TestCase(unittest.Testcase):
	
	def test_add_1(self):
		self.assertEqual(example.add(1,2), 3)


if __name__ == '__main__':
	unittest.main()
