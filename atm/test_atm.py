# test_atm.py

# By: Daniel A. Hagen
# Last Modified: 10/07/2020

import pytest
import unittest
import mock
from unittest import mock
from unittest import TestCase
import io
import sys

from atm import *


class Test_ATM(unittest.TestCase):

    def test_ATM__init__1(self):
        try:
            testATM = ATM()
        except:
            self.fail("ATM() raised Error unexpectedly!")

    def test_ATM__init__2(self):
        testATM = ATM()
        assert testATM.cardInserted==False, "No card should be detected when initialized."

    def test_card_inserted_good_1(self):
        try:
            testATM = ATM()
            testATM.card_inserted()
        except:
            self.fail("ATM.card_inserted() raised Error unexpectedly!")

    def test_card_inserted_good_2(self):
        testATM = ATM()
        testATM.card_inserted()
        assert testATM.cardInserted == True, "ATM.cardInserted should be positive."
        assert hasattr(testATM,"cardNumber"), "ATM should now have attr 'cardNumber'"
        assert testATM.cardNumber=="1234-5678-9101-1121", "Error with default cardNumber value."

    def test_card_inserted_good_3(self):
        testATM = ATM()
        testATM.card_inserted(cardNumber="1212-3434-5656-7878")
        assert testATM.cardInserted == True, "ATM.cardInserted should be positive."
        assert hasattr(testATM,"cardNumber"), "ATM should now have attr 'cardNumber'"
        assert testATM.cardNumber=="1212-3434-5656-7878", "Error with custom cardNumber value."

    def test_card_inserted_bad_1(self):
        testATM = ATM()
        self.assertRaises(
            AssertionError,
            testATM.card_inserted,
            cardNumber="aaaa-1111-1111-1111"
        )

    def test_card_inserted_bad_2(self):
        testATM = ATM()
        self.assertRaises(
            AssertionError,
            testATM.card_inserted,
            cardNumber="111-111-111-111"
        )

    def test_card_inserted_bad_3(self):
        testATM = ATM()
        self.assertRaises(
            AssertionError,
            testATM.card_inserted,
            cardNumber=1111111111111111
        )

    @mock.patch('atm.input', create=True)
    def test_detect_card_Y(self, mocked_input):
        mocked_input.side_effect = ['Y']
        testATM = ATM()
        testATM.card_inserted()
        cardInserted,exitProgram = testATM.detect_card()
        self.assertEqual(cardInserted,True)
        self.assertEqual(exitProgram,False)

    @mock.patch('atm.input', create=True)
    def test_detect_card_N(self, mocked_input):
        mocked_input.side_effect = ['N']
        testATM = ATM()
        testATM.card_inserted()
        cardInserted,exitProgram = testATM.detect_card()
        self.assertEqual(cardInserted,False)
        self.assertEqual(exitProgram,False)

    @mock.patch('atm.input', create=True)
    def test_detect_card_Exit_1(self, mocked_input):
        mocked_input.side_effect = ['Exit']
        testATM = ATM()
        testATM.card_inserted()
        cardInserted,exitProgram = testATM.detect_card()
        self.assertEqual(cardInserted,"Exit")
        self.assertEqual(exitProgram,True)

    @mock.patch('atm.input', create=True)
    def test_detect_card_Exit_2(self, mocked_input):
        mocked_input.side_effect = ['']
        testATM = ATM()
        testATM.card_inserted()
        cardInserted,exitProgram = testATM.detect_card()
        self.assertEqual(cardInserted,"")
        self.assertEqual(exitProgram,True)

    @mock.patch('atm.input', create=True)
    def test_detect_card_bad(self, mocked_input):
        mocked_input.side_effect = ['bad','y']
        testATM = ATM()
        testATM.card_inserted()
        cardInserted,exitProgram = testATM.detect_card()
        self.assertEqual(cardInserted,True)
        self.assertEqual(exitProgram,False)

    def test_card_removed_good(self):
        testATM = ATM()
        testATM.card_inserted(cardNumber="1212-3434-5656-7878")
        testATM.accountInfo = "Some Info"
        testATM.card_removed()
        assert not hasattr(testATM,"cardNumber"), "There should not longer be a cardNumber on file"
        assert not hasattr(testATM,"accountInfo"), "There should not longer be accountInfo on file"

    def test_get_card_number_good(self):
        testATM = ATM()
        testATM.get_card_number("1111")
        assert testATM.cardNumber=="1111", "Error assigning cardNumber"

    @mock.patch('atm.input', create=True)
    def test_input_pin_good(self, mocked_input):
        mocked_input.side_effect = ['1111']
        testATM = ATM()
        testATM.card_inserted()
        exitProgram = testATM.input_pin()
        self.assertEqual(testATM.PIN,"1111")
        self.assertEqual(exitProgram,False)

    @mock.patch('atm.input', create=True)
    def test_input_pin_Exit(self, mocked_input):
        mocked_input.side_effect = ['Exit']
        testATM = ATM()
        testATM.card_inserted()
        exitProgram = testATM.input_pin()
        self.assertEqual(testATM.PIN,"Exit")
        self.assertEqual(exitProgram,True)
        assert not hasattr(testATM,"cardNumber"), "ATM should not have a cardNumber"

    @mock.patch('atm.input', create=True)
    def test_input_pin_gibberish(self, mocked_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        mocked_input.side_effect = ['gibberish','9999']
        testATM = ATM()
        testATM.card_inserted()
        exitProgram = testATM.input_pin()
        self.assertEqual(
            capturedOutput.getvalue(),
            "Invalid PIN. Please enter Again.\n"
        )

    def test_is_pin_correct_bad_account(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        testATM = ATM()
        testATM.card_inserted(cardNumber="1111-1111-1111-1111")
        result = testATM.is_pin_correct(1)
        self.assertEqual(
            capturedOutput.getvalue(),
            "Not a valid account number...\nHave a nice day!\n"
        )

    def test_is_pin_correct_too_many_attempts(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        testATM = ATM()
        testATM.card_inserted()
        testATM.PIN = "1111"
        result = testATM.is_pin_correct(4)
        self.assertEqual(result,False)

    def test_is_pin_correct_good(self):
        testATM = ATM()
        testATM.card_inserted(cardNumber="1234-5678-9101-1121")
        testATM.PIN = "9999"
        attempts = 0
        result = testATM.is_pin_correct(attempts)
        assert result == True, "Error with testing if PIN is correct."

    def test_is_pin_correct_bad(self):
        testATM = ATM()
        testATM.card_inserted(cardNumber="1234-5678-9101-1121")
        testATM.PIN = "1111"
        attempts = 0
        result = testATM.is_pin_correct(attempts)
        assert result == False, "Error with testing if PIN is incorrect."

    @mock.patch('atm.input', create=True)
    def test_choose_account_1(self, mocked_input):
        mocked_input.side_effect = ['1']
        testATM = ATM()
        testATM.card_inserted()
        testATM.PIN = "9999"
        testATM.is_pin_correct(0)
        selectedAccount,exitProgram = testATM.choose_an_account()
        self.assertEqual(selectedAccount,"Savings Account")
        self.assertEqual(exitProgram,False)

    @mock.patch('atm.input', create=True)
    def test_choose_account_2(self, mocked_input):
        mocked_input.side_effect = ['2']
        testATM = ATM()
        testATM.card_inserted()
        testATM.PIN = "9999"
        testATM.is_pin_correct(0)
        selectedAccount,exitProgram = testATM.choose_an_account()
        self.assertEqual(selectedAccount,"Checking Account")
        self.assertEqual(exitProgram,False)

    @mock.patch('atm.input', create=True)
    def test_choose_account_3(self, mocked_input):
        mocked_input.side_effect = ['3']
        testATM = ATM()
        testATM.card_inserted()
        testATM.PIN = "9999"
        testATM.is_pin_correct(0)
        selectedAccount,exitProgram = testATM.choose_an_account()
        self.assertEqual(selectedAccount,"Carl's College Fund")
        self.assertEqual(exitProgram,False)

    @mock.patch('atm.input', create=True)
    def test_choose_account_Exit(self, mocked_input):
        mocked_input.side_effect = ['Exit']
        testATM = ATM()
        testATM.card_inserted()
        testATM.PIN = "9999"
        testATM.is_pin_correct(0)
        selectedAccount,exitProgram = testATM.choose_an_account()
        self.assertEqual(selectedAccount,None)
        self.assertEqual(exitProgram,True)

    def test_return_balance_good(self):
        testATM = ATM()
        testATM.accountInfo = {"Checking Account" : 100}
        assert testATM.return_balance("Checking Account")==100, "Error returning account balance"

    def test_return_balance_bad_1(self):
        testATM = ATM()
        self.assertRaises(AssertionError,testATM.return_balance,"Wrong Account")

    def test_return_balance_bad_2(self):
        testATM = ATM()
        testATM.accountInfo = {"Checking Account" : 100}
        self.assertRaises(AssertionError,testATM.return_balance,"Wrong Account")

    def test_make_deposit_good(self):
        testATM = ATM()
        testATM.accountInfo = {"Checking Account" : 100}
        testATM.make_deposit("Checking Account",100)
        assert testATM.return_balance("Checking Account")==200, "Error depositing to account"

    def test_make_deposit_bad_1(self):
        testATM = ATM()
        self.assertRaises(AssertionError,testATM.make_deposit,"Wrong Account",0)

    def test_make_deposit_bad_2(self):
        testATM = ATM()
        testATM.accountInfo = {"Checking Account" : 100}
        self.assertRaises(AssertionError,testATM.make_deposit,"Wrong Account",0)

    def test_make_withdrawal_good(self):
        testATM = ATM()
        testATM.accountInfo = {"Checking Account" : 100}
        testATM.make_withdrawal("Checking Account",100)
        assert testATM.return_balance("Checking Account")==0, "Error depositing to account"

    def test_make_withdrawal_bad_1(self):
        testATM = ATM()
        self.assertRaises(AssertionError,testATM.make_withdrawal,"Wrong Account",0)

    def test_make_withdrawal_bad_2(self):
        testATM = ATM()
        testATM.accountInfo = {"Checking Account" : 100}
        self.assertRaises(AssertionError,testATM.make_withdrawal,"Wrong Account",0)
