import unittest
import requests

import main as prog

url = 'https://brickset.com/sets/year-2007'
r = requests.get('https://brickset.com/sets/year-2007')


class Testing(unittest.TestCase):

    def test_login_requests(self):
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
