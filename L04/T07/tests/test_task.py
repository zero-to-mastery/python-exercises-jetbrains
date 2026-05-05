import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch


def try_import():
    return importlib.import_module('task')


class TestCase(unittest.TestCase):
    task_name = 'task'

    def setUp(self):
        try:
            with patch('sys.stdout', new=StringIO()):
                if self.task_name in sys.modules:
                    del sys.modules[self.task_name]
                task_file = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'task.py'
                )
                spec = importlib.util.spec_from_file_location(self.task_name, task_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[self.task_name] = module
        except NameError:
            pass
        except Exception as e:
            self.fail(
                "There was a problem while loading the solution — {0}. "
                "Check the solution for IDE-highlighted errors and warnings."
                .format(str(e))
            )

    def test_valid_user(self):
        try:
            module = try_import()
        except AttributeError:
            self.fail(msg="The function message_friends seems to be undefined.")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            module.message_friends({'name': 'Sorna', 'valid': True})

        self.assertEqual(
            fake_out.getvalue().strip(),
            'message has been sent',
            msg="A valid user should be able to send a message."
        )

    def test_invalid_user(self):
        try:
            module = try_import()
        except AttributeError:
            self.fail(msg="The function message_friends seems to be undefined.")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            module.message_friends({'name': 'Sorna', 'valid': False})

        self.assertEqual(
            fake_out.getvalue().strip(),
            'invalid user',
            msg="An invalid user should see 'invalid user'."
        )


if __name__ == '__main__':
    unittest.main()