# -*- coding: utf-8 -*-

import unittest
from calc import calculate

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

# summation
    def testSumInt(self):
        self.assertEqual(calculate('+', 2, 4), 6)

    def testSumFloatNum(self):
        self.assertEqual(calculate('+', 0.1, 0.2), 0.3)

    def testSumFloatNumInverce(self):
        self.assertEqual(calculate('+', 0.2, 0.1), 0.3)

    def testSumNegative(self):
        self.assertEqual(calculate('+', -10, 1), -9)


 # subtraction
    def testSubInt(self):
        self.assertEqual(calculate('-', 2, 4), -2)

    def testSubFloatNum(self):
        self.assertEqual(calculate('-', 0.1, 0.2), -0.1)

    def testSubFloatNumInverce(self):
        self.assertEqual(calculate('-', 0.2, 0.1), 0.1)

    def testSubNegative(self):
        self.assertEqual(calculate('-', 10, -1), 11)


# multiply
    def testMultiplyInt(self):
        self.assertEqual(calculate('*', 2, 4), 8)

    def testMultiplyFloatNum(self):
        self.assertEqual(calculate('*', 0.1, 0.2), 0.02)

    def testMultiplyFloatNumInverce(self):
        self.assertEqual(calculate('*', 0.2, 0.1), 0.02)

    def testMultiplyNegative(self):
        self.assertEqual(calculate('*', 10, -1), -10)

    def testMultiplyFloatMore1(self):
        self.assertEqual(calculate('*', 10.1, 0.1), 1.01)


# division
    def testDevInt(self):
        self.assertEqual(calculate('/', 2, 4), 0.5)

    def testDevFloatNum(self):
        self.assertEqual(calculate('/', 0.1, 0.2), 0.5)

    def testDevFloatNumInverce(self):
        self.assertEqual(calculate('/', 0.2, 0.1), 2.0)

    def testDevNegative(self):
        self.assertEqual(calculate('/', 10, -1), -10)

    def testDevFloatMore1(self):
        self.assertEqual(calculate('/', 10.1, 0.1), 101.0)


# pow
    def testPowInt(self):
        self.assertEqual(calculate('^', 2, 3), 8)

    def testPowFloatNum(self):
        self.assertEqual(calculate('^', 0.1, 2), 0.01)

    def testPowNumInverce(self):
        self.assertEqual(calculate('^', 3, 2), 9)

    def testPowNegative(self):
        self.assertEqual(calculate('^', 10, -1), 0.1)

    def testPowFloatMore1(self):
        self.assertEqual(calculate('^', 10.1, 2), 102.01)

    def testPowZero(self):
        self.assertEqual(calculate('^', 15, 0), 1)

# wrongs
    def testDevisionByZero(self):
        self.assertEqual(calculate('/', 2, 0), 'Error: Wow, wow. You are not God to do so things! (Divide on zero)')

    def testUnknownOperator(self):
        self.assertEqual(calculate('@', 1, 1), 'Error: It is useless calculator, and it do not know this operator((')

    def testSubNotNum(self):
        self.assertEqual(calculate('-', 'abc', 1), 'Error: It works just only with numbers')

    def testSubNotNumInverce(self):
        self.assertEqual(calculate('-', 1, 'abc'), 'Error: It works just only with numbers')

    # def testArgumentless(self):
    #     self.assertEqual(calculate('*', 1, ), 'Error: It needs 2 arguments')
    #
    # def testEmptyArgs(self):
    #     self.assertEqualtestArgumentless(calculate('^'), 'Error: It needs 2 arguments')

    def testNone(self):
        self.assertEqual(calculate('/', None, 1), 'Error: It works just only with numbers')

    def testNoneInverce(self):
        self.assertEqual(calculate('/', 1, None), 'Error: It works just only with numbers')