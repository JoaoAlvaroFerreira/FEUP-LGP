"""Simple test to demo test environment"""
from django.test import TestCase


class SimpleTestCase(TestCase):
    """
    A simple test case to demo the unit test environment
    """

    def setUp(self):
        self.value = 1

    def test_simple(self):
        """
        Simple test method
        """
        self.assertTrue(self.value)
