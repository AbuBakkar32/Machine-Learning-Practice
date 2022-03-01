import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = 10
        b = 20
        self.assertEqual(a + b, 30)
        self.assertIsInstance(a, int)

    def test_2(self):
        name = "selenium"
        title = "Selenium in a automating world"
        assert name.lower() in title.lower()
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
