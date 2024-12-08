import unittest
from src.main.stablecoin.reserve_management import ReserveManagement

class TestReserveManagement(unittest.TestCase):

    def setUp(self):
        self.rm = ReserveManagement()

    def test_add_reserve(self):
        initial_reserve = self.rm.get_total_reserve()
        self.rm.add_reserve(1000)
        new_reserve = self.rm.get_total_reserve()
        self.assertGreater(new_reserve, initial_reserve)

    def test_withdraw_reserve(self):
        self.rm.add_reserve(1000)
        initial_reserve = self.rm.get_total_reserve()
        self.rm.withdraw_reserve(500)
        new_reserve = self.rm.get_total_reserve()
        self.assertEqual(new_reserve, initial_reserve - 500)

if __name__ == '__main__':
    unittest.main()
