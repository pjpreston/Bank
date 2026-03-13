import unittest

from bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def test_account_belongs_to_customer(self):
        account = BankAccount("Alice")

        self.assertEqual(account.customer, "Alice")

    def test_add_cash_increases_balance(self):
        account = BankAccount("Alice")

        balance = account.add_cash(50)

        self.assertEqual(balance, 50)
        self.assertEqual(account.balance, 50)

    def test_withdraw_cash_reduces_balance(self):
        account = BankAccount("Alice", 100)

        balance = account.withdraw_cash(40)

        self.assertEqual(balance, 60)
        self.assertEqual(account.balance, 60)

    def test_cannot_overdraw_account(self):
        account = BankAccount("Alice", 25)

        with self.assertRaisesRegex(ValueError, "Insufficient funds."):
            account.withdraw_cash(30)

    def test_opening_balance_cannot_be_negative(self):
        with self.assertRaisesRegex(ValueError, "Opening balance cannot be negative."):
            BankAccount("Alice", -1)

    def test_customer_is_required(self):
        with self.assertRaisesRegex(ValueError, "Customer is required."):
            BankAccount("")

    def test_deposit_must_be_positive(self):
        account = BankAccount("Alice")

        with self.assertRaisesRegex(ValueError, "Deposit amount must be greater than zero."):
            account.add_cash(0)

    def test_withdrawal_must_be_positive(self):
        account = BankAccount("Alice", 20)

        with self.assertRaisesRegex(ValueError, "Withdrawal amount must be greater than zero."):
            account.withdraw_cash(0)


if __name__ == "__main__":
    unittest.main()
