from django.test import TestCase


# Create your tests here.
class BasicTest(TestCase):
    def test_basic_case(self):
        print("here goes")
        self.assertTrue(True, "This shouldn't ever fail")


# Create your tests here.
class BasicTestTwo(TestCase):
    def test_basic_case(self):
        print("here goes")
        self.assertTrue(True, "This shouldn't ever fail")
