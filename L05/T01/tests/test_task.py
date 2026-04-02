import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch


class TestCase(unittest.TestCase):
    task_name = 'task'

    def load_module(self, argv, inputs, randint_value):
        task_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'task.py'
        )

        if self.task_name in sys.modules:
            del sys.modules[self.task_name]

        spec = importlib.util.spec_from_file_location(self.task_name, task_file)
        module = importlib.util.module_from_spec(spec)
        output = StringIO()

        try:
            with patch.object(sys, 'argv', argv), \
                 patch('builtins.input', side_effect=inputs), \
                 patch('sys.stdout', new=output), \
                 patch('random.randint', return_value=randint_value):
                spec.loader.exec_module(module)
        except StopIteration:
            self.fail(
                "The program asked for more input than expected. "
                "Make sure the loop continues after wrong answers and stops after the correct guess."
            )
        except SyntaxError:
            self.fail(
                "There is a syntax error in your code. Check your if statement."
            )

        return output.getvalue()

    def test_uses_command_line_arguments_1_10(self):
        task_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'task.py'
        )

        if self.task_name in sys.modules:
            del sys.modules[self.task_name]

        spec = importlib.util.spec_from_file_location(self.task_name, task_file)
        module = importlib.util.module_from_spec(spec)

        with patch.object(sys, 'argv', ['task.py', '1', '10']), \
             patch('builtins.input', side_effect=['5']), \
             patch('sys.stdout', new=StringIO()), \
             patch('random.randint', return_value=5) as mocked_randint:
            spec.loader.exec_module(module)

        if mocked_randint.call_args[0] != (1, 10):
            self.fail("Use the command-line arguments as the boundaries for randint().")

    def test_uses_command_line_arguments_4_9(self):
        task_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'task.py'
        )

        if self.task_name in sys.modules:
            del sys.modules[self.task_name]

        spec = importlib.util.spec_from_file_location(self.task_name, task_file)
        module = importlib.util.module_from_spec(spec)

        with patch.object(sys, 'argv', ['task.py', '4', '9']), \
             patch('builtins.input', side_effect=['6']), \
             patch('sys.stdout', new=StringIO()), \
             patch('random.randint', return_value=6) as mocked_randint:
            spec.loader.exec_module(module)

        if mocked_randint.call_args[0] != (4, 9):
            self.fail("Use the command-line arguments as the boundaries for randint().")

    def test_wrong_answers_then_correct_answer(self):
        output = self.load_module(['task.py', '1', '10'], ['15', '4', '7'], 7)

        self.assertIn(
            "You're a genius!",
            output,
            msg="The game should continue after wrong answers and stop after the correct guess."
        )

    def test_invalid_input_then_correct_answer(self):
        output = self.load_module(['task.py', '1', '10'], ['hello', '3', '5'], 5)

        self.assertIn(
            "Please enter a number",
            output,
            msg="Print an error message if the input is not a number."
        )

        self.assertIn(
            "You're a genius!",
            output,
            msg="After invalid input, the game should continue until the correct guess."
        )


if __name__ == '__main__':
    unittest.main()