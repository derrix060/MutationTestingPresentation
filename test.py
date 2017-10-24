import unittest
from bank import BankAccount

class BadTestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount("TestName", 0)
        self.account_1 = BankAccount('For testing', 100)
        self.account_2 = BankAccount('In dollars', 10)

    def test_deposit_positive_amount(self):
        self.account.deposit(10)
        self.assertEqual(self.account._balance, 10)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_positive_amount(self):
        self.account.deposit(100)

        result = self.account.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(self.account._balance, 50)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_transfer_positive_amount(self):
        self.account_1.transfer_to(self.account_2, 50)

        self.assertEqual(self.account_1._balance, 50)
        self.assertEqual(self.account_2._balance, 60)

    def test_withdraw_from_empty_account(self):
        result = self.account.withdraw(50)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        assert "Withdraw for 50 failed" in self.account._history

class GoodTestBankAccount():
# class GoodTestBankAccount(unittest.TestCase): # Uncomment this line to run the good test

    def setUp(self):
        self.account = BankAccount("TestName", 0)

    def test_blank(self):
        self.assertTrue(True)

    def test_deposit_minimum_amount(self):
        self.account.deposit(1)
        self.assertEqual(self.account._balance, 1)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_positive_amount_min(self):
        self.account.deposit(100)
        result = self.account.withdraw(99)
        self.assertTrue(result)
        self.assertEqual(self.account._balance, 1)

    def test_withdraw_positive_amount_max(self):
        self.account.deposit(100)
        result = self.account.withdraw(1)
        self.assertTrue(result)
        self.assertEqual(self.account._balance, 99)

    def test_withdraw_maximum_amount(self):
        self.account.deposit(100)
        result = self.account.withdraw(100)
        self.assertTrue(result)
        self.assertEqual(self.account._balance, 0)

    def test_transfer_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account_1.transfer_to(self.account_2, -50)
        self.assertEqual(self.account_1._balance, 100)
        self.assertEqual(self.account_2._balance, 10)

if __name__ == '__main__':
    unittest.main(verbosity=2)