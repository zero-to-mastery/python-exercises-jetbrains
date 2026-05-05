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

    def test_chilli_class_exists(self):
        try:
            module = try_import()
            Chilli = module.Chilli
            Cat = module.Cat
        except AttributeError:
            self.fail(msg="The class Chilli seems to be undefined.")

        self.assertTrue(
            issubclass(Chilli, Cat),
            msg="Chilli should inherit from Cat."
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

    def test_cat_instance_types(self):
        try:
            module = try_import()
            Simon = module.Simon
            Sally = module.Sally
            Chilli = module.Chilli
            cat1 = module.cat1
            cat2 = module.cat2
            cat3 = module.cat3
        except AttributeError:
            self.fail(msg="Make sure Simon, Sally, Chilli, cat1, cat2, and cat3 are defined.")

        self.assertIsInstance(cat1, Simon, msg="cat1 should be an instance of Simon.")
        self.assertIsInstance(cat2, Sally, msg="cat2 should be an instance of Sally.")
        self.assertIsInstance(cat3, Chilli, msg="cat3 should be an instance of Chilli.")

    def test_my_pets_instance(self):
        try:
            module = try_import()
            Pets = module.Pets
            my_pets = module.my_pets
            my_cats = module.my_cats
        except AttributeError:
            self.fail(msg="Make sure Pets, my_pets, and my_cats are defined.")

        self.assertIsInstance(my_pets, Pets, msg="my_pets should be an instance of Pets.")
        self.assertEqual(my_pets.animals, my_cats, msg="my_pets should be created with my_cats.")

    def test_answer_value(self):
        expected_value = [
            "Simon is just walking around",
            "Sally is just walking around",
            "Chilli is just walking around"
        ]

        try:
            actual_value = try_import().answer
        except AttributeError:
            self.fail(msg="The variable answer seems to be undefined.")

        self.assertEqual(
            actual_value,
            expected_value,
            msg="answer should contain the walking results for all cats."
        )


if __name__ == '__main__':
    unittest.main()