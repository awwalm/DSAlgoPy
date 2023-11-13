import unittest
from Goodrich.Chapter9.Exercises.Creativity.C_9_26 import PriorityStack


class TestStackMethods(unittest.TestCase):

    def setUp(self):
        self.s = PriorityStack()

    def test_empty_function_on_empty_stack(self):
        self.assertTrue(self.s.is_empty())
        self.assertEqual(0, self.s.size)

    def test_empty_function_with_items_in_stack(self):
        self.s.push(1)
        self.assertFalse(self.s.is_empty())

    def test_pop_function_on_empty_stack(self):
        with self.assertRaises(IndexError) as c:
            self.s.pop()
        self.assertTrue('Stack Empty' in str(c.exception))

    def test_pop_function_with_items_in_stack(self):
        self.s.push(1)
        self.assertEqual(1, self.s.pop())

    def test_peek_function_on_empty_stack(self):
        self.assertIs(self.s.peek(), None)

    def test_peek_function_with_items_in_stack(self):
        self.s.push(1)
        self.s.push(2)
        self.assertEqual(2, self.s.peek())

    def test_push_function_for_one_item(self):
        self.s.push(10)
        self.assertEqual(1, self.s.size)

    def test_push_function_on_a_list_arg(self):
        args = [1, 2, 3, 4]
        for arg in args:
            self.s.push(arg)
        self.assertEqual(4, self.s.size)

    def test_push_function_on_multiple_args(self):
        for i in 1, 2, 3, 4:
            self.s.push(i)
        self.assertEqual(4, self.s.size)

    def test_lifo_functionality(self):
        for i in 1, 2, 3, 4:
            self.s.push(i)
        self.assertEqual(4, self.s.pop())
        self.assertEqual(3, self.s.pop())
        self.assertEqual(2, self.s.pop())
        self.assertEqual(1, self.s.pop())
        self.assertTrue(self.s.is_empty())


if __name__ == '__main__':
    unittest.main()
