from sendgrid.helpers.mail.validators import ValidateAPIKey
from sendgrid.helpers.mail.exceptions import APIKeyIncludedException

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestValidateAPIKey(unittest.TestCase):

    def test_basic_validator_initialization(self):
        validator = ValidateAPIKey()
        self.assertIsInstance(validator.regexes, set)
        self.assertEqual(len(validator.regexes), 1)

    def test_validator_with_own_regexes(self):
        validator = ValidateAPIKey(regex_strings=['test_one', 'test_two'])
        self.assertEqual(len(validator.regexes), 3)

    def test_validator_no_default(self):
        validator = ValidateAPIKey(use_default=False)
        self.assertEqual(len(validator.regexes), 0)

    def test_can_add_regexes(self):
        validator = ValidateAPIKey(use_default=False)
        validator.regexes.add('test')
        self.assertIsInstance(validator.regexes, set)
        self.assertEqual(len(validator.regexes), 1)


    def test_validate_message_text_passes(self):
        validator = ValidateAPIKey(regex_strings=['test_one'])
        validator.validate_message_text('test_two')

    def test_validate_message_text_raises_exception(self):
        validator = ValidateAPIKey(regex_strings=['test_one'])
        with self.assertRaises(APIKeyIncludedException):
            validator.validate_message_text('test_one')

    def test_validate_message_dict_passes(self):
        validator = ValidateAPIKey(regex_strings=['test_one'])
        test_dict = {
            "content": [{
                "type": "txt/html",
                "value": "test_two"
            }]
        }
        validator.validate_message_dict(test_dict)

    def test_validate_message_dict_raises_exception(self):
        validator = ValidateAPIKey(regex_strings=['test_one'])
        test_dict = {
            "content": [{
                "type": "txt/html",
                "value": "test_one"
            }]
        }
        with self.assertRaises(APIKeyIncludedException):
            validator.validate_message_dict(test_dict)

    def test_validate_message_dict_text_edge_case_passes(self):
        validator = ValidateAPIKey(regex_strings=['test_one'])
        test_message = "test_two"
        validator.validate_message_dict(test_message)

    def test_validate_message_dict_text_edge_case_raises_exception(self):
        validator = ValidateAPIKey(regex_strings=['test_one'])
        test_message = "test_one"
        with self.assertRaises(APIKeyIncludedException):
            validator.validate_message_dict(test_message)
