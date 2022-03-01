from unittest import TestCase
from unittest.mock import patch

import HTMLTestRunner


class TestBlog(TestCase):
    @patch('utestfile.file.main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        assert MockBlog.called  # The mock wasP called
        blog.posts.assert_called_with()  # We called the posts' method with no arguments
        blog.posts.assert_called_once_with()  # We called the posts method once with no arguments
        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts
        # with no arguments
        blog.reset_mock()  # Reset the mock object
        blog.posts.assert_not_called()  # After resetting, posts has not been called.


if __name__ == '__main__':
    HTMLTestRunner.main()
    # unittest.main(
    #     testRunner=xmlrunner.XMLTestRunner(output='test-reports'), failfast=False, buffer=True, catchbreak=False)

# def mock_sum(a, b):
#     # mock sum function without the long-running time.sleep
#     return a + b
#
#
# class TestCalculator(TestCase):
#     def setUp(self):
#         self.calc = main.Calculator()
#
#     def test_sum(self):
#         answer = self.calc.sum(2, 4)
#         self.assertEqual(answer, 6)
#
#     @patch('main.Calculator.sum', side_effect=mock_sum)
#     def test_sum(self, sum):
#         self.assertEqual(sum(2, 3), 5)
#         self.assertEqual(sum(7, 3), 10)
