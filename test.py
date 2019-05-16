import unittest
import marketbeat_scraper as mb
import user_defined_exceptions


class TestMarketBeat(unittest.TestCase):
    def test_date_na(self):
        self.assertListEqual(mb.run("2019-04-13"), [])

    def test_date_earlier(self):
        self.assertListEqual(mb.run("2018-12-13"), [])

    def test_date_later(self):
        self.assertListEqual(mb.run("2030-04-03"), [])

    def test_dict(self):
        self.assertIsInstance(mb.run("2019-02-20")[0], dict)

    def test_num_dict(self):
        self.assertEqual(len(mb.run("2019-02-20")), 99)


if __name__ == "__main__":
    unittest.main()
