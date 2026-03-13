import unittest

from bank_account import Bank, Account


class BankAccountTests(unittest.TestCase):
    def test_account_has_unique_integer_account_number(self):
        first_account = Account("Alice")
        second_account = Account("Bob")

        self.assertIsInstance(first_account.account_number, int)
        self.assertIsInstance(second_account.account_number, int)
        self.assertNotEqual(first_account.account_number, second_account.account_number)

    def test_account_belongs_to_customer(self):
        account = Account("Alice")

        self.assertEqual(account.customer, "Alice")

    def test_add_cash_increases_balance(self):
        account = Account("Alice")

        balance = account.add_cash(50)

        self.assertEqual(balance, 50)
        self.assertEqual(account.balance, 50)

    def test_withdraw_cash_reduces_balance(self):
        account = Account("Alice", 100)

        balance = account.withdraw_cash(40)

        self.assertEqual(balance, 60)
        self.assertEqual(account.balance, 60)

    def test_cannot_overdraw_account(self):
        account = Account("Alice", 25)

        with self.assertRaisesRegex(ValueError, "Insufficient funds."):
            account.withdraw_cash(30)

    def test_opening_balance_cannot_be_negative(self):
        with self.assertRaisesRegex(ValueError, "Opening balance cannot be negative."):
            Account("Alice", -1)

    def test_customer_is_required(self):
        with self.assertRaisesRegex(ValueError, "Customer is required."):
            Account("")

    def test_deposit_must_be_positive(self):
        account = Account("Alice")

        with self.assertRaisesRegex(ValueError, "Deposit amount must be greater than zero."):
            account.add_cash(0)

    def test_withdrawal_must_be_positive(self):
        account = Account("Alice", 20)

        with self.assertRaisesRegex(ValueError, "Withdrawal amount must be greater than zero."):
            account.withdraw_cash(0)


class BankTests(unittest.TestCase):
    def test_bank_stores_accounts_by_account_number(self):
        bank = Bank()
        account = Account("Alice")

        bank.add_account(account)

        self.assertEqual(bank.accounts, {account.account_number: account})

    def test_bank_can_get_account_by_account_number(self):
        bank = Bank()
        account = Account("Alice")
        bank.add_account(account)

        stored_account = bank.get_account(account.account_number)

        self.assertIs(stored_account, account)


if __name__ == "__main__":
    unittest.main()
