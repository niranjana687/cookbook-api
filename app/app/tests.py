from django.test import TestCase

from app.calc import add

def CalcTests(Testcase):

    def sometest_add_numbers(self):
        """Test that two numbers are added togther"""
        self.assertEqual(add(5,5), 10)