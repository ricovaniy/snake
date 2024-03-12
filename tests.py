import unittest
import game


class TestTest(unittest.TestCase):
    def test_merge(self):
        logs = open("logs.txt")
        logs_length = len(logs.readlines())
        game.read_settings("setting_test.txt")
        logs.close()
        new_logs = open("logs.txt")
        self.assertEqual(logs_length + 1, len(new_logs.readlines()))
        new_logs.close()


if __name__ == "__main__":
    unittest.main()