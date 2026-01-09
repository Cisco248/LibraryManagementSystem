"""
Module: test_module

This module contains test cases for demonstrating unittest functionality,
along with class methods and instance methods for testing purposes.
"""
import unittest

class TestHello:
    """
    Test case class for demonstrating instance methods.
    """

    @classmethod
    def callme(cls):
        """
        Class method for printing a call message.
        """
        print("callme called!")

    def test_method1(self):
        """
        Instance method for testing the first method.
        """
        print("test_method1 called")

    def test_method2(self):
        """
        Instance method for testing the second method.
        """
        print("test_method2 called")

class TestOther:
    """
    Test case class for demonstrating another set of instance methods.
    """

    @classmethod
    def callme(cls):
        """
        Class method for printing another call message.
        """
        print("callme other called")

    def test_other(self):
        """
        Instance method for testing the 'other' method.
        """
        print("test other")

class SomeTest(unittest.TestCase):
    """
    Unit test case class for unittest demonstration.
    """
    @classmethod
    def callme(cls):
        """
        Class method for printing a call message for unittest case.
        """
        print("SomeTest callme called")

    def test_unit1(self):
        """
        Instance method for testing a unittest method.
        """
        print("test_unit1 method called")

# Add final newline