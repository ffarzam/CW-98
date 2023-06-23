import re
import unittest


class EmailValidator:
    @classmethod
    def is_valid(self, email):
        pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-z0-9.-]+[.]\S{2,3}$"
        match = re.match(pattern, email)
        return bool(match)


class TestEmailValidator(unittest.TestCase):

    def test_email_valid(self):
        self.assertTrue(EmailValidator.is_valid("ffarzam_1992@yahoo.com"))

    def test_email_invalid(self):
        self.assertFalse(EmailValidator.is_valid("ffarzam_1992@com"))


if __name__ == '__main__':
    unittest.main()
