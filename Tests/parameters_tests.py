import unittest
import addition


class MyTestCase(unittest.TestCase):
    def test_addition_smaller_first(self):
        """
        You will use this function as a template for your own tests. You don't need to know what most of this means
        for right now, but the important thing is to change two lines: the addition.add_two() and the assert output
        lines. Everything else can stay the same.
        :return:
        """
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(2, 4)
            output = out.getvalue().strip()
            assert output == "The sum of 2 and 4 is 6"
        finally:
            sys.stdout = saved_stdout

    def test_addition_larger_first(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(12, 9)
            output = out.getvalue().strip()
            assert output == "The sum of 12 and 9 is 21"
        finally:
            sys.stdout = saved_stdout

    def test_adding_one_negative(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(-3, 7)
            output = out.getvalue().strip()
            assert output == "The sum of -3 and 7 is 4"
        finally:
            sys.stdout = saved_stdout

    def test_adding_two_negatives(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(-6, -13)
            output = out.getvalue().strip()
            assert output == "The sum of -6 and -13 is -19"
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
