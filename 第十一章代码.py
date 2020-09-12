def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

import unittest
class NamesTestCase(unittest.TestCase):
    "测试"
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jains', 'joplin')
        self.assertEqual(formatted_name, 'Jains Joplin')
unittest.main()