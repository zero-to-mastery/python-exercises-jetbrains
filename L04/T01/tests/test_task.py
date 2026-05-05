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

    def test_cat_instances_exist(self):
        try:
            module = try_import()
            cat1 = module.cat1
            cat2 = module.cat2
            cat3 = module.cat3
        except AttributeError:
            self.fail(msg="Make sure cat1, cat2, and cat3 are defined.")

        self.assertIsNotNone(cat1, msg="cat1 should not be None.")
        self.assertIsNotNone(cat2, msg="cat2 should not be None.")
        self.assertIsNotNone(cat3, msg="cat3 should not be None.")

    def test_cat_instances_type(self):
        try:
            module = try_import()
            Cat = module.Cat
            cat1 = module.cat1
            cat2 = module.cat2
            cat3 = module.cat3
        except AttributeError:
            self.fail(msg="Make sure Cat, cat1, cat2, and cat3 are defined.")

        self.assertIsInstance(cat1, Cat, msg="cat1 should be an instance of Cat.")
        self.assertIsInstance(cat2, Cat, msg="cat2 should be an instance of Cat.")
        self.assertIsInstance(cat3, Cat, msg="cat3 should be an instance of Cat.")

    def test_cat_ages(self):
        try:
            module = try_import()
            cat1 = module.cat1
            cat2 = module.cat2
            cat3 = module.cat3
        except AttributeError:
            self.fail(msg="Make sure cat1, cat2, and cat3 are defined.")

        self.assertEqual(cat1.age, 5, msg="The first Cat should have age 5.")
        self.assertEqual(cat2.age, 1, msg="The second Cat should have age 1.")
        self.assertEqual(cat3.age, 8, msg="The third Cat should have age 8.")

    def test_oldest_cat_function(self):
        try:
            oldest_cat = try_import().oldest_cat
        except AttributeError:
            self.fail(msg="The function oldest_cat seems to be undefined.")

        result = oldest_cat(5, 1, 8)
        self.assertEqual(
            result,
            8,
            msg="The function oldest_cat should return 8 for the ages 5, 1, and 8."
        )

    def test_oldest_age_value(self):
        try:
            actual_value = try_import().oldest_age
        except AttributeError:
            self.fail(msg="The variable oldest_age seems to be undefined.")

        self.assertEqual(
            actual_value,
            8,
            msg="oldest_age should store the value 8."
        )


if __name__ == '__main__':
    unittest.main()