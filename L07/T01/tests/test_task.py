import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import MagicMock, patch


class TestCase(unittest.TestCase):
    task_name = 'task'

    def setUp(self):
        self.smtp_instance = MagicMock()
        self.smtp_class = MagicMock()
        self.smtp_class.return_value.__enter__.return_value = self.smtp_instance

        try:
            with patch('sys.stdout', new=StringIO()) as self.actualOutput, \
                 patch('pathlib.Path.read_text', return_value='<h1>Hello, $name!</h1>'), \
                 patch('smtplib.SMTP', self.smtp_class):

                if self.task_name in sys.modules:
                    self.module = importlib.reload(sys.modules[self.task_name])
                else:
                    self.module = importlib.import_module(self.task_name)

        except NameError:
            pass
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_email_content_is_set_as_html(self):
        actual_email = self.module.email

        self.assertEqual(
            actual_email.get_content_subtype(),
            'html',
            msg="The email body was not set as HTML. Make sure you call a method on the email object "
                "to set the HTML content."
        )

    def test_name_is_substituted_into_template(self):
        actual_email = self.module.email
        actual_content = actual_email.get_content()

        self.assertIn(
            'TinTin',
            actual_content,
            msg="The name 'TinTin' is missing from the email body. Make sure you use substitute() "
                "to set name to 'TinTin' in the HTML template."
        )

    def test_placeholder_is_replaced_in_template(self):
        actual_email = self.module.email
        actual_content = actual_email.get_content()

        self.assertNotIn(
            '$name',
            actual_content,
            msg="The placeholder '$name' is still present in the email body. Make sure you replace "
                "the placeholder before setting the content."
        )

    def test_smtp_connection_is_created_with_gmail_and_port_587(self):
        self.smtp_class.assert_called_once_with(host='smtp.gmail.com', port=587)

    def test_smtp_connects_to_server(self):
        self.smtp_instance.ehlo.assert_called_once_with()

    def test_smtp_starts_secure_connection(self):
        self.smtp_instance.starttls.assert_called_once_with()