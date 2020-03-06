# -*- coding: utf-8 -*-
import unittest

from sendgrid.helpers.mail import (Email)


class TestEmailObject(unittest.TestCase):

    def test_add_email_address(self):
        address = "test@example.com"
        email = Email(address)

        self.assertEqual(email.email, "test@example.com")

    def test_add_name(self):
        name = "SomeName"
        email = Email(name=name)

        self.assertEqual(email.name, name)

    def test_add_unicode_name(self):
        name = u"SomeName"
        email = Email(name=name)

        self.assertEqual(email.name, name)

    def test_add_name_email(self):
        name = "SomeName"
        address = "test@example.com"
        email = Email(email=address, name=name)
        self.assertEqual(email.name, name)
        self.assertEqual(email.email, "test@example.com")

    def test_add_unicode_name_email(self):
        name = u"SomeName"
        address = u"test@example.com"
        email = Email(email=address, name=name)
        self.assertEqual(email.name, name)
        self.assertEqual(email.email, u"test@example.com")

    def test_add_rfc_function_finds_name_not_email(self):
        name = "SomeName"
        email = Email(name)

        self.assertEqual(email.name, name)
        self.assertIsNone(email.email)

    def test_add_rfc_email(self):
        name = "SomeName"
        address = "test@example.com"
        name_address = "{} <{}>".format(name, address)
        email = Email(name_address)
        self.assertEqual(email.name, name)
        self.assertEqual(email.email, "test@example.com")

    def test_empty_obj_add_name(self):
        email = Email()
        name = "SomeName"
        email.name = name

        self.assertEqual(email.name, name)

    def test_empty_obj_add_email(self):
        email = Email()
        address = "test@example.com"
        email.email = address

        self.assertEqual(email.email, address)

    def test_add_name_with_comma(self):
        email = Email()
        name = "Name, Some"
        email.name = name

        self.assertEqual(email.name, '"' + name + '"')

    def test_add_unicode_name_with_comma(self):
        email = Email()
        name = u"Name, Some"
        email.name = name

        self.assertEqual(email.name, u'"' + name + u'"')

    def test_equality_email_name(self):
        address = "test@example.com"
        name = "SomeName"
        email1 = Email(address, name)
        email2 = Email(address, name)
        
        self.assertEqual(email1, email2)

    def test_equality_email(self):
        address = "test@example.com"
        email1 = Email(address)
        email2 = Email(address)
        
        self.assertEqual(email1, email2)

    def test_equality_name(self):
        name = "SomeName"
        email1 = Email()
        email1.name = name
        email2 = Email()
        email2.name = name

        self.assertEqual(email1, email2)

    def test_equality_different_emails(self):
        address1 = "test1@example.com"
        email1 = Email(address1)
        address2 = "test2@example.com"
        email2 = Email(address2)

        self.assertNotEqual(email1, email2)

    def test_equality_different_name(self):
        name1 = "SomeName1"
        email1 = Email()
        email1.name = name1
        name2 = "SomeName2"
        email2 = Email()
        email2.name = name2

        self.assertNotEqual(email1, email2)

    def test_equality_non_email(self):
        address = "test@example.com"
        email = Email(address)

        self.assertNotEqual(email, address)
