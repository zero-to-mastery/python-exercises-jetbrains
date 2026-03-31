import importlib
import sys
import unittest


def try_import():
    from L06.T01 import task
    return task


class TestCase(unittest.TestCase):
    task_name = 'L06.T01.task'

    def setUp(self):
        try:
            if self.task_name in sys.modules:
                self.task = importlib.reload(sys.modules[self.task_name])
            else:
                self.task = importlib.import_module(self.task_name)
        except NameError as ne:
            pass
        except ModuleNotFoundError:
            self.fail("All 4 tests in test.py must pass. Check that you have implemented do_stuff() function correctly.")
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_all_test_cases_pass(self):
        """Verify that all 4 tests in test.py exist and pass"""
        from L06.T01.tests import test

        # Check at least 4 tests exist
        test_methods = [method for method in dir(test.TestDoStuff)
                        if method.startswith('test_')]
        self.assertGreaterEqual(len(test_methods), 4,
                               "test.py must contain at least 4 test methods")

        # Check all tests pass
        suite = unittest.TestLoader().loadTestsFromModule(test)
        runner = unittest.TextTestRunner(stream=None, verbosity=0)
        result = runner.run(suite)

        if result.errors:
            failed_test = result.errors[0][0].id().split('.')[-1]
            self.fail(f"Test `{failed_test}` in test.py raised an error. Check that you have implemented do_stuff() function correctly.")

        if result.failures:
            failed_test = result.failures[0][0].id().split('.')[-1]
            self.fail(f"Test `{failed_test}` in test.py failed. Check that you have implemented do_stuff() function correctly.")


if __name__ == '__main__':
    unittest.main()
