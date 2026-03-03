import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestSetsExercise(unittest.TestCase):
    """Tests for Sets Exercise."""

    @classmethod
    def setUpClass(cls):
        """Import the student's code once before all tests."""
        cls.import_error = None
        cls.module = None

        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "student_code",
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "12-ExerciseSets.py")
            )
            cls.module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cls.module)
        except NameError as e:
        except SyntaxError as e:
            cls.import_error = f"Syntax error in your code: {e}"
        except Exception as e:
            cls.import_error = f"Error loading your code: {e}"

    def test_code_runs(self):
        """Test that the code executes without errors."""
        if self.import_error:
            self.fail(self.import_error)

        # Basic check that module loaded
        self.assertIsNotNone(self.module)


if __name__ == '__main__':
    unittest.main()
